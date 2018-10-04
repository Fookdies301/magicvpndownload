from gevent import monkey
monkey.patch_all()

import logging


from create_app import create_app


"""
runs the flask app
"""
app = create_app('etc.settings')
logging.root.setLevel(logging.DEBUG)
logging.disable(0)
