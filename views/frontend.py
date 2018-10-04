import time

import os
from flask import (Blueprint, render_template, request,
                   send_from_directory, jsonify, send_file)

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
    # time.sleep(8)
    # return send_from_directory(directory=os.path.join('downloads'),
    #                            filename=filename)
    print(os.path.join('downloads', filename))
    return send_file(os.path.join('downloads', filename), as_attachment=True,
                     add_etags=True, attachment_filename=filename)


@frontend.route('/test', methods=['GET'])
def test():
    filename = request.args.get('file_name')
    print(os.listdir('downloads'))
    return send_file(os.path.join('downloads', filename), as_attachment=True,
                     add_etags=True, attachment_filename=filename)
