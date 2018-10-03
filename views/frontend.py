from flask import Blueprint, render_template, request, send_file

from utils.file_handler import download_file as download

frontend = Blueprint('frontend', __name__)


@frontend.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@frontend.route('/download_file', methods=['GET', 'POST'])
def download_file():
    url = request.form.get('url_to_download')
    filename = request.form.get('file_name')
    download(url, filename)
    return 'Downloaded'
    # return send_file(scraped_data_file, as_attachment=True, add_etags=True,
    #                  attachment_filename=filename)
