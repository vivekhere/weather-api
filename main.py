from fastapi import FastAPI
from views import home
from api import weather_api
from config import settings

app = FastAPI()

app.include_router(home.router)
app.include_router(weather_api.router)
