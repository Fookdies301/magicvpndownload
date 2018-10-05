from flask import (Blueprint, render_template, request,
                   jsonify)

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
    temp_link = download(url, filename)
    if not temp_link:
        return jsonify({'message': 'Incorrect resource'})
    return jsonify({'message': 'Downloaded', 'file_link': temp_link})
