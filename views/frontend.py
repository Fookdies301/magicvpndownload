import time

import os
from flask import (Blueprint, render_template, request,
                   send_from_directory, jsonify, send_file)
from openpyxl import load_workbook

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
    return jsonify({'message': 'Downloaded'})


@frontend.route('/test', methods=['GET'])
def test():
    filename = request.args.get('file_name')
    print(os.listdir('downloads'))
    # abs_path = os.path.join('/app/downloads', filename)
    # print(abs_path)
    scraped_data_file = os.path.join('downloads',
                                     filename)
    print('***download location %r' % scraped_data_file)
    wb = load_workbook('document.xlsx')
    wb.save(scraped_data_file, as_template=True)
    return send_from_directory(filename=scraped_data_file, as_attachment=True)
    # return send_file(abs_path,
    #                  mimetype='application/vnd.ms-excel',
    #                  attachment_filename=filename,
    #                  as_attachment=True)
    # return send_file(abs_path, as_attachment=True,
    #                  add_etags=True, attachment_filename=filename)
