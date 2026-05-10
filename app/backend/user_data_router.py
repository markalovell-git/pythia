from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, field_validator
from sqlalchemy.orm import Session
from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
import uuid

from app.common.database import get_db, UserData, UserSettings, NatalChart
from app.common.constants import DEFAULT_ZODIAC_SYSTEM

user_data_router = APIRouter()


class UserInputBase(BaseModel):
    name: str
    birth_datetime: datetime
    birth_timezone: str
    birth_location: str
    birth_lat: float
    birth_lon: float

    @field_validator("birth_timezone")
    @classmethod
    def validate_timezone(cls, v: str) -> str:
        try:
            ZoneInfo(v)
        except ZoneInfoNotFoundError:
            raise ValueError(f"Unknown timezone: {v!r}. Use an IANA timezone name e.g. 'America/Chicago'.")
        return v

    @field_validator("birth_lat")
    @classmethod
    def validate_lat(cls, v: float) -> float:
        if not -90 <= v <= 90:
            raise ValueError("birth_lat must be between -90 and 90")
        return v

    @field_validator("birth_lon")
    @classmethod
    def validate_lon(cls, v: float) -> float:
        if not -180 <= v <= 180:
            raise ValueError("birth_lon must be between -180 and 180")
        return v


class UserInput(UserInputBase):
    username: str


class UserUpdateInput(UserInputBase):
    pass


@user_data_router.post("/submit_user_data")
async def submit_user_data(user_input: UserInput, db: Session = Depends(get_db)):
    if db.query(UserData).filter(UserData.username == user_input.username).first():
        raise HTTPException(status_code=409, detail="Username already exists")
    user_id = str(uuid.uuid4())
    db.add(UserData(
        user_id=user_id,
        username=user_input.username,
        name=user_input.name,
        birth_datetime=user_input.birth_datetime,
        birth_timezone=user_input.birth_timezone,
        birth_location=user_input.birth_location,
        birth_lat=user_input.birth_lat,
        birth_lon=user_input.birth_lon,
    ))
    db.add(UserSettings(user_id=user_id, zodiac_system=DEFAULT_ZODIAC_SYSTEM))
    db.commit()
    return {
        "message": "User data submitted successfully",
        "user_id": user_id,
        "user_data": user_input.model_dump(),
    }


@user_data_router.put("/update_user_data/{user_id}")
async def update_user_data(user_id: str, user_input: UserUpdateInput, db: Session = Depends(get_db)):
    record = db.query(UserData).filter(UserData.user_id == user_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="User not found")
    record.name = user_input.name
    record.birth_datetime = user_input.birth_datetime
    record.birth_timezone = user_input.birth_timezone
    record.birth_location = user_input.birth_location
    record.birth_lat = user_input.birth_lat
    record.birth_lon = user_input.birth_lon
    chart = db.query(NatalChart).filter(NatalChart.user_id == user_id).first()
    if chart:
        db.delete(chart)
    db.commit()
    return {"message": "User data updated successfully", "user_id": user_id}


@user_data_router.get("/get_user_data/{user_id}")
async def get_user_data(user_id: str, db: Session = Depends(get_db)):
    record = db.query(UserData).filter(UserData.user_id == user_id).first()
    if record is None:
        raise HTTPException(status_code=404, detail="User data not found")
    return {
        "user_data": {
            "username": record.username,
            "name": record.name,
            "birth_datetime": record.birth_datetime,
            "birth_timezone": record.birth_timezone,
            "birth_location": record.birth_location,
            "birth_lat": record.birth_lat,
            "birth_lon": record.birth_lon,
        }
    }


@user_data_router.get("/list_users")
async def list_users(db: Session = Depends(get_db)):
    records = db.query(UserData).all()
    return [
        {"user_id": r.user_id, "username": r.username, "name": r.name}
        for r in records
    ]


@user_data_router.delete("/delete_user/{user_id}")
async def delete_user(user_id: str, db: Session = Depends(get_db)):
    record = db.query(UserData).filter(UserData.user_id == user_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(record)
    db.commit()
    return {"message": "User deleted successfully", "user_id": user_id}


@user_data_router.get("/get_user_by_username/{username}")
async def get_user_by_username(username: str, db: Session = Depends(get_db)):
    record = db.query(UserData).filter(UserData.username == username).first()
    if record is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {
        "user_id": record.user_id,
        "username": record.username,
        "name": record.name,
        "birth_datetime": record.birth_datetime,
        "birth_timezone": record.birth_timezone,
        "birth_location": record.birth_location,
        "birth_lat": record.birth_lat,
        "birth_lon": record.birth_lon,
    }
