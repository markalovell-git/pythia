from sqlalchemy import create_engine, Column, String, DateTime, Float, ForeignKey, JSON
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class UserData(Base):
    __tablename__ = "user_data"

    user_id = Column(String, primary_key=True, index=True)
    username = Column(String, nullable=False, unique=True, index=True)
    name = Column(String, nullable=False)
    birth_datetime = Column(DateTime, nullable=False)
    birth_timezone = Column(String, nullable=False)
    birth_location = Column(String, nullable=False)
    birth_lat = Column(Float, nullable=False)
    birth_lon = Column(Float, nullable=False)

    settings = relationship("UserSettings", back_populates="user", uselist=False, cascade="all, delete-orphan")
    natal_chart = relationship("NatalChart", back_populates="user", uselist=False, cascade="all, delete-orphan")


class UserSettings(Base):
    __tablename__ = "user_settings"

    user_id = Column(String, ForeignKey("user_data.user_id"), primary_key=True)
    zodiac_system = Column(String, nullable=False)

    user = relationship("UserData", back_populates="settings")


class NatalChart(Base):
    __tablename__ = "natal_charts"

    user_id = Column(String, ForeignKey("user_data.user_id"), primary_key=True)
    computed_at = Column(DateTime, nullable=False)
    positions = Column(JSON, nullable=False)

    user = relationship("UserData", back_populates="natal_chart")


Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
