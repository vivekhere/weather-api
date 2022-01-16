from fastapi import FastAPI
from views import home
from api import weather_api

app = FastAPI()

app.include_router(home.router)
app.include_router(weather_api.router)
