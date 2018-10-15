#!/usr/bin/env python

from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS


def create_app(config_filename):
    """
        Creates an app reading the config file
    """
    global app

    app = Flask(__name__)
    cors = CORS(app)
    app.config.from_object(config_filename)
    from views.frontend import frontend
    app.register_blueprint(frontend)
    limiter = Limiter(
        app,
        key_func=get_remote_address,
        default_limits=["5 per minute", "10 per hour", "20 per day"]
    )
    return app
