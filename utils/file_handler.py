import time

import dropbox
import os
import requests
import threading
from dropbox.files import WriteMode

from utils.helper import max_file_size_in_byte, max_file_size_in_mb


def download_file(url, filename):
    """
        Downloads file from the url and save it as filename
    """
    temp_link = ''
    # check if file already exists
    if not os.path.isfile(filename):
        print('Downloading File')
        response = requests.get(url)
        # Check if the response is ok (200)
        if response.status_code == 200:
            if float(response.headers.get('Content-Length')) > \
                    max_file_size_in_byte():
                return 'Only up to %s MB is allowed' % max_file_size_in_mb()
            # Open file and write the content
            filename = os.path.join('downloads', filename)
            with open(filename, 'wb') as file:
                # A chunk of 128 bytes
                for chunk in response:
                    file.write(chunk)
                file.close()
            temp_link = upload_file(filename)
        else:
            return 'Not a valid link'
    else:
        print('File exists')
    print('Completed download in server')
    return temp_link


def upload_file(file_path):
    """
    Uploads file to dropbox temporarily
    :param file_path: str; location of file to upload
    :return: str; temporary link of the file in dropbox
    """
    token = os.environ.get('TOKEN_KEY')
    client = dropbox.Dropbox(token)
    f = open(file_path, 'rb')
    filename = file_path.rsplit('/', 1)[-1]
    remote_file_path = '/' + filename
    response = client.files_upload(f.read(), remote_file_path,
                                   mode=WriteMode('overwrite'))
    f.close()
    print('Response = %r' % response)
    t1 = threading.Thread(target=remove_file, args=(client, remote_file_path))
    t1.start()
    return client.files_get_temporary_link(remote_file_path).link


def remove_file(client, file_path):
    """
    Runs as a thread
    Deletes file from dropbox after some time
    :param client: dropbox client object
    :param file_path: path of the file in dropbox to delete
    :return:
    """
    counter = int(os.environ.get('DELETE_IN_SECONDS', 30))
    while counter > 1:
        time.sleep(1)
        counter -= 1
        print('Deleting in %d seconds' % counter)
    client.files_delete_v2(file_path)
