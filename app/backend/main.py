from fastapi import FastAPI
from app.backend.user_data_router import user_data_router
from app.backend.user_settings_router import user_settings_router
from app.backend.chart_router import chart_router
from app.backend.geocode_router import geocode_router

app = FastAPI()
app.include_router(user_data_router, prefix="/api")
app.include_router(user_settings_router, prefix="/api")
app.include_router(chart_router, prefix="/api")
app.include_router(geocode_router, prefix="/api")
