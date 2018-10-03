import time

import os
from flask import (Blueprint, render_template, request,
                   send_from_directory, jsonify)

from utils.file_handler import download_file as download

frontend = Blueprint('frontend', __name__)


@frontend.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@frontend.route('/download_file', methods=['GET', 'POST'])
def download_file():
    url = request.form.get('url_to_download')
    filename = request.form.get('file_name')
    if not (url and filename):
        return jsonify({'message': 'Illegal input fileds'})
    download(url, filename)
    print('**** before download')
    print(os.listdir('downloads'))
    time.sleep(4)
    # return send_from_directory(directory=os.path.join('downloads'),
    #                            filename=filename)
    return jsonify({'message': 'Downloaded %s' % filename})


@frontend.route('/test', methods=['GET', 'POST'])
def test():
    return send_from_directory(directory=os.path.join('downloads'),
                               filename='.gitkeep')