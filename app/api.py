import os
import requests
from .utils import load_airports
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENTRIPMAP_API_KEY")

def get_airport_coords(code):
    airports = load_airports()
    airport = airports.get(code.upper())
    if airport:
        return airport['lat'], airport['lon']
    return None

def get_nearby_places(coords, transit_minutes):
    lat, lon = coords
    radius = 10000  # meters

    url = f"https://api.opentripmap.com/0.1/en/places/radius"
    params = {
        "radius": radius,
        "lon": lon,
        "lat": lat,
        "rate": 2,
        "format": "json",
        "limit": 30,
        "apikey": API_KEY
    }

    res = requests.get(url, params=params)
    if res.status_code == 200:
        return res.json()
    return []
