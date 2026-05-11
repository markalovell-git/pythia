from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.common.database import get_db, UserData, UserSettings, NatalChart
from app.common.constants import VALID_ZODIAC_SYSTEMS, VALID_HOUSE_SYSTEMS

user_settings_router = APIRouter()


class SettingsUpdate(BaseModel):
    zodiac_system: str | None = None
    house_system: str | None = None


@user_settings_router.get("/get_user_settings/{user_id}")
async def get_user_settings(user_id: str, db: Session = Depends(get_db)):
    if not db.query(UserData).filter(UserData.user_id == user_id).first():
        raise HTTPException(status_code=404, detail="User not found")
    settings = db.query(UserSettings).filter(UserSettings.user_id == user_id).first()
    return {
        "user_id":       user_id,
        "zodiac_system": settings.zodiac_system,
        "house_system":  settings.house_system,
    }


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
    chart = db.query(NatalChart).filter(NatalChart.user_id == user_id).first()
    if chart:
        db.delete(chart)
    db.commit()
    return {
        "user_id":       user_id,
        "zodiac_system": settings.zodiac_system,
        "house_system":  settings.house_system,
    }
