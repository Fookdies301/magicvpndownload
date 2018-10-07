#!/usr/bin/env python

import logging
from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


def create_app(config_filename):
    """
        Creates an app reading the config file
    """
    global app

    app = Flask(__name__)
    app.config.from_object(config_filename)
    # _configure_logging(app)
    from views.frontend import frontend
    app.register_blueprint(frontend)
    limiter = Limiter(app, key_func=get_remote_address,
                      default_limits=["5 per minute"])

    return app


def _configure_logging(app):
    level = getattr(logging, 'INFO')
    logging.root.setLevel(level)
    logging.disable(level - 1)
    logging.root.addHandler(_create_console_logger())


def _create_console_logger():
    stderr_format = "%(levelname)s: %(message)s"
    stderr_handler = logging.StreamHandler()
    stderr_handler.setFormatter(logging.Formatter(stderr_format))
    return stderr_handler
