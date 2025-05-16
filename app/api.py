import os
import requests
from .utils import load_airports
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENTRIPMAP_API_KEY")

def get_airport_coords(code):
    airports = load_airports()
    code = code.upper()
    for airport in airports:
        if airport['iata'] == code:
            return float(airport['Latitude']), float(airport['Longitude'])
    return None

# def get_nearby_places(coords, transit_minutes):
#     lat, lon = coords
#     radius = 10000  # meters

#     url = f"https://api.opentripmap.com/0.1/en/places/radius"
#     params = {
#         "radius": radius,
#         "lon": lon,
#         "lat": lat,
#         "rate": 2,
#         "format": "json",
#         "limit": 30,
#         "apikey": API_KEY
#     }

#     res = requests.get(url, params=params)
#     if res.status_code == 200:
#         return res.json()
#     return []

def get_nearby_places(lat, lon, time):
    radius = int(time) * 80  # Estimate ~80 meters per minute walking
    if radius > 10000:
        radius = 10000  # OpenTripMap API limit

    kinds = "interesting_places,tourist_facilities,cultural,historic,architecture,museums,foods,pubs"

    url = f"https://api.opentripmap.com/0.1/en/places/radius"
    params = {
        "radius": radius,
        "lon": lon,
        "lat": lat,
        "kinds": kinds,
        "format": "json",
        "limit": 50,
        "apikey": API_KEY
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return []
