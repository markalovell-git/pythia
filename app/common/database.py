import logging as _logging

from sqlalchemy import create_engine, Column, String, DateTime, Float, Integer, ForeignKey, JSON, Date, text
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

from app.common import paths

_log = _logging.getLogger(__name__)

SQLALCHEMY_DATABASE_URL = f"sqlite:///{paths.db_path()}"
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


class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id         = Column(Integer, primary_key=True, autoincrement=True)
    user_id    = Column(String, ForeignKey("user_data.user_id"), index=True, nullable=False)
    role       = Column(String, nullable=False)   # "user" | "assistant"
    content    = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)

    user = relationship("UserData")


class DiaryEntry(Base):
    __tablename__ = "diary_entries"

    entry_id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("user_data.user_id"), nullable=False, index=True)
    entry_date = Column(Date, nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)


def init_db() -> None:
    """Create tables and apply column migrations against the real database.

    Called once at backend startup — not at import — so merely importing this
    module (e.g. in tests, which use their own engine) never touches the user's
    database on disk.
    """
    paths.migrate_legacy_db()
    Base.metadata.create_all(bind=engine)

    # Migrate existing databases that predate AI settings columns.
    with engine.connect() as conn:
        for col, dflt in [
            ("ai_provider",   "'ollama'"),
            ("anthropic_key", "NULL"),
            ("openai_key",    "NULL"),
            ("ollama_url",    "'http://localhost:11434'"),
            ("ollama_model",  "'qwen3:14b'"),
        ]:
            try:
                conn.execute(text(
                    f"ALTER TABLE user_settings ADD COLUMN {col} TEXT DEFAULT {dflt}"
                ))
                conn.commit()
            except Exception as e:
                if "duplicate column name" not in str(e).lower():
                    _log.error("Migration failed adding column %s: %s", col, e)

    _migrate_plaintext_api_keys()


def _migrate_plaintext_api_keys() -> None:
    """Move legacy plaintext API keys into the keyring (or encrypted column)."""
    from app.common import secrets

    db = SessionLocal()
    try:
        for row in db.query(UserSettings).all():
            changed = False
            for provider, col in (("anthropic", "anthropic_key"), ("openai", "openai_key")):
                moved, new_value = secrets.migrate_plaintext_value(
                    row.user_id, provider, getattr(row, col)
                )
                if moved:
                    setattr(row, col, new_value)
                    changed = True
            if changed:
                _log.info("Moved plaintext API key(s) to protected storage for %s", row.user_id)
        db.commit()
    finally:
        db.close()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
