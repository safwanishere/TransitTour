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
    code = request.args.get("airport")
    hours = int(request.args.get("hours"))
    minutes = int(request.args.get("minutes"))

    time = hours * 60 + minutes;

    coords = get_airport_coords(code)
    if not coords:
        return "Invalid airport code", 400

    lat, lon = coords
    places = get_nearby_places(lat, lon, time)
    return render_template("plan.html", lat=lat, lon=lon, places=places, code=code)

@routes.route('/about')
def about():
    return render_template("about.html")