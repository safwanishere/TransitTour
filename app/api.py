import os
import requests
from .utils import load_airports, get_image_url
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


def get_nearby_places(lat, lon, time):
    radius = int(time) * 50
    if radius > 10000:
        radius = 10000  # OpenTripMap API limit

    kinds = "interesting_places,cultural,historic,architecture,museums,foods,pubs"

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
        places = response.json()

        # for place in places:
        #     name = place['name']
        #     url = get_image_url(name)
        #     place['url'] = url

        return places
    return []
