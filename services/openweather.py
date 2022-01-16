from typing import Optional
from fastapi import HTTPException
from config import settings
import httpx


async def get_weather_report(city: str, state: Optional[str], country: str, units: str) -> dict:
    q = f"{city},{country}"
    if state:
        q = f"{city},{state},{country}"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={q}&appid={settings.ow_key}&units={units}"

    async with httpx.AsyncClient() as client:
        res: httpx.Response = await client.get(url)
        if res.status_code != 200:
            raise HTTPException(status_code=res.status_code, detail=res.text)

    return res.json()["main"]
