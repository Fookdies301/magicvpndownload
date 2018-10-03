from flask import Blueprint, render_template, request

from utils.file_handler import download_file as download

frontend = Blueprint('frontend', __name__)


@frontend.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@frontend.route('/download_file', methods=['GET', 'POST'])
def download_file():
    print(request.form.get('url_to_download'))
    url = 'https://www.dmepdac.com/docs/crosswalk/october_18/2018-10-05XWalkFinalVersion.xlsx'
    filename = url.rsplit('/', 1)[1]
    download(url, filename)
    return 'Downloaded'
