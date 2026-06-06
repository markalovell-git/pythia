from datetime import datetime, date, timezone

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.common.database import get_db, UserData, ConsultCache, ChatMessage

consult_router = APIRouter()

_LONGER_TERM_DAYS = 7


def _is_valid(entry: ConsultCache) -> bool:
    now = datetime.now(timezone.utc).replace(tzinfo=None)
    if entry.horizon == "today":
        return entry.cached_at.date() == now.date()  # both UTC — avoids local/UTC date mismatch
    return (now - entry.cached_at).days < _LONGER_TERM_DAYS


@consult_router.get("/consult_cache/{user_id}/{horizon}")
async def get_consult_cache(user_id: str, horizon: str, db: Session = Depends(get_db)):
    if horizon not in ("today", "longer_term"):
        raise HTTPException(status_code=422, detail="horizon must be 'today' or 'longer_term'")
    if not db.query(UserData).filter(UserData.user_id == user_id).first():
        raise HTTPException(status_code=404, detail="User not found")
    entry = (
        db.query(ConsultCache)
        .filter(ConsultCache.user_id == user_id, ConsultCache.horizon == horizon)
        .first()
    )
    if entry is None or not _is_valid(entry):
        raise HTTPException(status_code=404, detail="No valid cache entry")
    return {"content": entry.content, "cached_at": entry.cached_at.isoformat()}


class CacheBody(BaseModel):
    content: str


@consult_router.put("/consult_cache/{user_id}/{horizon}")
async def set_consult_cache(
    user_id: str, horizon: str, body: CacheBody, db: Session = Depends(get_db)
):
    if horizon not in ("today", "longer_term"):
        raise HTTPException(status_code=422, detail="horizon must be 'today' or 'longer_term'")
    if not db.query(UserData).filter(UserData.user_id == user_id).first():
        raise HTTPException(status_code=404, detail="User not found")
    entry = (
        db.query(ConsultCache)
        .filter(ConsultCache.user_id == user_id, ConsultCache.horizon == horizon)
        .first()
    )
    now = datetime.now(timezone.utc).replace(tzinfo=None)
    if entry is None:
        entry = ConsultCache(user_id=user_id, horizon=horizon, cached_at=now, content=body.content)
        db.add(entry)
    else:
        entry.cached_at = now
        entry.content = body.content
    db.commit()
    return {"status": "ok"}


# ── Chat history ────────────────────────────────────────────────────────────────

def _require_user(user_id: str, db: Session) -> None:
    if not db.query(UserData).filter(UserData.user_id == user_id).first():
        raise HTTPException(status_code=404, detail="User not found")


@consult_router.get("/chat_history/{user_id}")
async def get_chat_history(user_id: str, db: Session = Depends(get_db)):
    _require_user(user_id, db)
    rows = (
        db.query(ChatMessage)
        .filter(ChatMessage.user_id == user_id)
        .order_by(ChatMessage.id)
        .all()
    )
    return [{"role": r.role, "content": r.content} for r in rows]


class ChatMessageBody(BaseModel):
    role: str
    content: str


@consult_router.post("/chat_history/{user_id}")
async def append_chat_message(
    user_id: str, body: ChatMessageBody, db: Session = Depends(get_db)
):
    if body.role not in ("user", "assistant"):
        raise HTTPException(status_code=422, detail="role must be 'user' or 'assistant'")
    _require_user(user_id, db)
    now = datetime.now(timezone.utc).replace(tzinfo=None)
    db.add(ChatMessage(user_id=user_id, role=body.role, content=body.content, created_at=now))
    db.commit()
    return {"status": "ok"}


@consult_router.delete("/chat_history/{user_id}")
async def clear_chat_history(user_id: str, db: Session = Depends(get_db)):
    _require_user(user_id, db)
    db.query(ChatMessage).filter(ChatMessage.user_id == user_id).delete()
    db.commit()
    return {"status": "ok"}
