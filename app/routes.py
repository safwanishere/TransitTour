from flask import Blueprint, render_template, request
from .api import get_airport_coords, get_nearby_places

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/plan')
def plan():
    airport_code = request.args.get('airport')
    transit_minutes = int(request.args.get('time'))

    coords = get_airport_coords(airport_code)
    if not coords:
        return "Invalid airport code", 400

    places = get_nearby_places(coords, transit_minutes)
    return render_template('plan.html', coords=coords, places=places)
