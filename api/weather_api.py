from fastapi import APIRouter, Depends
from typing import Optional
from models.location import Location
from services import openweather

router = APIRouter()


@router.get("/api/weather/{city}")
async def weather(loc: Location = Depends(), units: Optional[str] = "metric"):
    report = await openweather.get_weather_report(loc.city, loc.state, loc.country, units)
    return report
