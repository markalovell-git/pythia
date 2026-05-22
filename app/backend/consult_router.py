from datetime import datetime, date, timezone

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.common.database import get_db, UserData, ConsultCache

consult_router = APIRouter()

_LONGER_TERM_DAYS = 7


def _is_valid(entry: ConsultCache) -> bool:
    now = datetime.now(timezone.utc).replace(tzinfo=None)
    if entry.horizon == "today":
        return entry.cached_at.date() == date.today()
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
