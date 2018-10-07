from flask import (Blueprint, request, jsonify, render_template)
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from utils.file_handler import download_file

frontend = Blueprint('frontend', __name__)


limiter = Limiter(frontend, key_func=get_remote_address,
                  default_limits=["5 per minute"])


@frontend.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@frontend.route('/download', methods=['GET'])
def download():
    filename = request.args.get('file_name')
    url = request.args.get('download_url')
    if not (url and filename):
        return jsonify({'message': 'Illegal input fields'})
    temp_link = download_file(url, filename)
    if not temp_link:
        return jsonify({'message': 'Incorrect resource'})
    return jsonify({'message': 'Downloaded', 'file_link': temp_link})
