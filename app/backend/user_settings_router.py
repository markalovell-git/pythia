from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.common import secrets
from app.common.database import get_db, UserData, UserSettings, NatalChart
from app.common.constants import (
    VALID_ZODIAC_SYSTEMS, VALID_HOUSE_SYSTEMS,
    DEFAULT_ANTHROPIC_MODEL, DEFAULT_OPENAI_MODEL,
    DEFAULT_OLLAMA_MODEL, DEFAULT_OLLAMA_URL,
)

user_settings_router = APIRouter()

# API keys are handled separately — they go through app.common.secrets
_AI_TEXT_FIELDS = (
    "ai_provider", "anthropic_model", "openai_model", "ollama_url", "ollama_model",
)


class SettingsUpdate(BaseModel):
    zodiac_system:   str | None = None
    house_system:    str | None = None
    ai_provider:     str | None = None
    anthropic_key:   str | None = None
    openai_key:      str | None = None
    anthropic_model: str | None = None
    openai_model:    str | None = None
    ollama_url:      str | None = None
    ollama_model:    str | None = None


def _settings_response(user_id: str, settings: UserSettings) -> dict:
    return {
        "user_id":         user_id,
        "zodiac_system":   settings.zodiac_system,
        "house_system":    settings.house_system,
        "ai_provider":     getattr(settings, "ai_provider",     "ollama"),
        "anthropic_key":   secrets.get_api_key(user_id, "anthropic", getattr(settings, "anthropic_key", None)),
        "openai_key":      secrets.get_api_key(user_id, "openai",    getattr(settings, "openai_key",    None)),
        "anthropic_model": getattr(settings, "anthropic_model", DEFAULT_ANTHROPIC_MODEL),
        "openai_model":    getattr(settings, "openai_model",    DEFAULT_OPENAI_MODEL),
        "ollama_url":      getattr(settings, "ollama_url",      DEFAULT_OLLAMA_URL),
        "ollama_model":    getattr(settings, "ollama_model",    DEFAULT_OLLAMA_MODEL),
    }


@user_settings_router.get("/get_user_settings/{user_id}")
async def get_user_settings(user_id: str, db: Session = Depends(get_db)):
    if not db.query(UserData).filter(UserData.user_id == user_id).first():
        raise HTTPException(status_code=404, detail="User not found")
    settings = db.query(UserSettings).filter(UserSettings.user_id == user_id).first()
    return _settings_response(user_id, settings)


@user_settings_router.put("/update_user_settings/{user_id}")
async def update_user_settings(
    user_id: str, update: SettingsUpdate, db: Session = Depends(get_db)
):
    if update.zodiac_system is not None and update.zodiac_system not in VALID_ZODIAC_SYSTEMS:
        raise HTTPException(
            status_code=422,
            detail=f"zodiac_system must be one of {sorted(VALID_ZODIAC_SYSTEMS)}",
        )
    if update.house_system is not None and update.house_system not in VALID_HOUSE_SYSTEMS:
        raise HTTPException(
            status_code=422,
            detail=f"house_system must be one of {sorted(VALID_HOUSE_SYSTEMS)}",
        )
    if not db.query(UserData).filter(UserData.user_id == user_id).first():
        raise HTTPException(status_code=404, detail="User not found")
    settings = db.query(UserSettings).filter(UserSettings.user_id == user_id).first()
    if update.zodiac_system is not None:
        settings.zodiac_system = update.zodiac_system
    if update.house_system is not None:
        settings.house_system = update.house_system
    # AI settings — changes do not invalidate the natal chart
    for field in _AI_TEXT_FIELDS:
        value = getattr(update, field)
        if value is not None:
            setattr(settings, field, value)
    # API keys go to the keyring when available; the column stores NULL or ciphertext
    if update.anthropic_key is not None:
        settings.anthropic_key = secrets.set_api_key(user_id, "anthropic", update.anthropic_key)
    if update.openai_key is not None:
        settings.openai_key = secrets.set_api_key(user_id, "openai", update.openai_key)
    # Only invalidate natal chart for zodiac/house changes
    if update.zodiac_system is not None or update.house_system is not None:
        chart = db.query(NatalChart).filter(NatalChart.user_id == user_id).first()
        if chart:
            db.delete(chart)
    db.commit()
    return _settings_response(user_id, settings)
