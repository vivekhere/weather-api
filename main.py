from fastapi import FastAPI
from views import home

app = FastAPI()

app.include_router(home.router)
