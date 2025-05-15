from flask import Flask, session
from flask_session import Session

def createApp():
    app = Flask(__name__)
    
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)

    from .routes import routes

    app.register_blueprint(routes, url_prefix="/")

    return app