from fastapi import FastAPI
from app.backend.user_data_router import user_data_router
from app.backend.user_settings_router import user_settings_router
from app.backend.chart_router import chart_router
from app.backend.geocode_router import geocode_router
from app.backend.diary_router import diary_router
from app.backend.locations_router import locations_router
from app.backend.consult_router import consult_router

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(user_data_router, prefix="/api")
app.include_router(user_settings_router, prefix="/api")
app.include_router(chart_router, prefix="/api")
app.include_router(geocode_router, prefix="/api")
app.include_router(diary_router, prefix="/api")
app.include_router(locations_router, prefix="/api")
app.include_router(consult_router, prefix="/api")
