import uuid
from datetime import datetime, date

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.common.database import get_db, UserData, DiaryEntry

diary_router = APIRouter()


class DiaryEntryCreate(BaseModel):
    entry_date: date
    content: str


class DiaryEntryUpdate(BaseModel):
    content: str


def _entry_response(entry: DiaryEntry) -> dict:
    return {
        "entry_id": entry.entry_id,
        "user_id": entry.user_id,
        "entry_date": str(entry.entry_date),
        "content": entry.content,
        "created_at": entry.created_at.isoformat(),
        "updated_at": entry.updated_at.isoformat(),
    }


@diary_router.get("/get_diary_entries/{user_id}")
async def get_diary_entries(
    user_id: str, date: date | None = None, db: Session = Depends(get_db)
):
    if not db.query(UserData).filter(UserData.user_id == user_id).first():
        raise HTTPException(status_code=404, detail="User not found")
    q = db.query(DiaryEntry).filter(DiaryEntry.user_id == user_id)
    if date:
        q = q.filter(DiaryEntry.entry_date == date)
    return [_entry_response(e) for e in q.order_by(DiaryEntry.entry_date).all()]


@diary_router.post("/create_diary_entry/{user_id}")
async def create_diary_entry(
    user_id: str, body: DiaryEntryCreate, db: Session = Depends(get_db)
):
    if not db.query(UserData).filter(UserData.user_id == user_id).first():
        raise HTTPException(status_code=404, detail="User not found")
    now = datetime.utcnow()
    entry = DiaryEntry(
        entry_id=str(uuid.uuid4()),
        user_id=user_id,
        entry_date=body.entry_date,
        content=body.content,
        created_at=now,
        updated_at=now,
    )
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return _entry_response(entry)


@diary_router.put("/update_diary_entry/{entry_id}")
async def update_diary_entry(
    entry_id: str, body: DiaryEntryUpdate, db: Session = Depends(get_db)
):
    entry = db.query(DiaryEntry).filter(DiaryEntry.entry_id == entry_id).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    entry.content = body.content
    entry.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(entry)
    return _entry_response(entry)


@diary_router.delete("/delete_diary_entry/{entry_id}")
async def delete_diary_entry(entry_id: str, db: Session = Depends(get_db)):
    entry = db.query(DiaryEntry).filter(DiaryEntry.entry_id == entry_id).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    db.delete(entry)
    db.commit()
    return {"entry_id": entry_id, "deleted": True}
