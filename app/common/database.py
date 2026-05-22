from sqlalchemy import create_engine, Column, String, DateTime, Float, ForeignKey, JSON, Date, text
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

    user_id       = Column(String, ForeignKey("user_data.user_id"), primary_key=True)
    zodiac_system = Column(String, nullable=False)
    house_system  = Column(String, nullable=False, default="placidus")
    ai_provider   = Column(String, nullable=False, default="ollama")
    anthropic_key = Column(String, nullable=True)
    openai_key    = Column(String, nullable=True)
    ollama_url    = Column(String, nullable=False, default="http://localhost:11434")
    ollama_model  = Column(String, nullable=False, default="qwen3:14b")

    user = relationship("UserData", back_populates="settings")


class NatalChart(Base):
    __tablename__ = "natal_charts"

    user_id = Column(String, ForeignKey("user_data.user_id"), primary_key=True)
    computed_at = Column(DateTime, nullable=False)
    positions = Column(JSON, nullable=False)
    house_cusps = Column(JSON, nullable=True)

    user = relationship("UserData", back_populates="natal_chart")


class ConsultCache(Base):
    __tablename__ = "consult_cache"

    user_id   = Column(String, ForeignKey("user_data.user_id"), primary_key=True)
    horizon   = Column(String, primary_key=True)  # "today" | "longer_term"
    cached_at = Column(DateTime, nullable=False)
    content   = Column(String, nullable=False)

    user = relationship("UserData")


class DiaryEntry(Base):
    __tablename__ = "diary_entries"

    entry_id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("user_data.user_id"), nullable=False, index=True)
    entry_date = Column(Date, nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)


Base.metadata.create_all(bind=engine)

# Migrate existing databases that predate AI settings columns
with engine.connect() as _conn:
    for _col, _dflt in [
        ("ai_provider",   "'ollama'"),
        ("anthropic_key", "NULL"),
        ("openai_key",    "NULL"),
        ("ollama_url",    "'http://localhost:11434'"),
        ("ollama_model",  "'qwen3:14b'"),
    ]:
        try:
            _conn.execute(text(
                f"ALTER TABLE user_settings ADD COLUMN {_col} TEXT DEFAULT {_dflt}"
            ))
            _conn.commit()
        except Exception:
            pass  # column already exists


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
