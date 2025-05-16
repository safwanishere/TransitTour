from flask import Blueprint, render_template, request
from .api import get_airport_coords, get_nearby_places
from app.utils import load_airports

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    airports = load_airports()
    return render_template('index.html', airports=airports)

@routes.route('/plan')
def plan():
    # airport_code = request.args.get('airport')
    # transit_minutes = int(request.args.get('time'))

    # coords = get_airport_coords(airport_code)
    # if not coords:
    #     return "Invalid airport code", 400

    # places = get_nearby_places(coords, transit_minutes)
    # return render_template('plan.html', coords=coords, places=places)

    code = request.args.get("airport")
    time = request.args.get("time", default="30")
    coords = get_airport_coords(code)
    if not coords:
        return "Invalid airport code", 400

    lat, lon = coords
    places = get_nearby_places(lat, lon, time)
    return render_template("plan.html", lat=lat, lon=lon, places=places)
