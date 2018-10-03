from flask import Blueprint, render_template, request, send_file, jsonify
import os
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
    return send_file(os.path.join('/app', filename),
                     as_attachment=True, add_etags=True,
                     attachment_filename=filename)
