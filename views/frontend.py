from flask import (Blueprint, request, jsonify, render_template, make_response)
from flask_limiter.util import get_remote_address

from utils.email_sender import send_email
from utils.file_handler import download_file

frontend = Blueprint('frontend', __name__)


@frontend.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@frontend.route('/download', methods=['POST'])
def download():
    filename = request.form.get('file_name')
    url = request.form.get('download_url')
    if not (url and filename):
        return jsonify({'message': 'Illegal input fields'})
    temp_link = download_file(url, filename)
    send_email(message='Generated file_link: %s' % temp_link,
               ip_address=get_remote_address())
    return jsonify({'file_link': temp_link})


@frontend.errorhandler(429)
def ratelimit_handler(e):
    return make_response(jsonify(error="Error=%s" % e.description), 429)
