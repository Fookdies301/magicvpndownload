import time

import os
from flask import (Blueprint, render_template, request,
                   send_from_directory, jsonify)

from utils.file_handler import download_file as download

frontend = Blueprint('frontend', __name__)


@frontend.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@frontend.route('/download_file', methods=['GET'])
def download_file():
    filename = request.args.get('file_name')
    url = request.args.get('download_url')
    if not (url and filename):
        return jsonify({'message': 'Illegal input fields'})
    download(url, filename)
    return send_from_directory(directory=os.path.join('downloads'),
                               filename=filename)
