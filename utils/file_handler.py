import os
import requests
import dropbox
from dropbox.files import WriteMode
import threading
import time


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
            # Open file and write the content
            filename = os.path.join('downloads', filename)
            with open(filename, 'wb') as file:
                # A chunk of 128 bytes
                for chunk in response:
                    file.write(chunk)
                file.close()
            temp_link = upload_file(filename)
    else:
        print('File exists')
    print('Completed download in server')
    return temp_link


def upload_file(file_path):
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


def remove_file(client, filepath):
    counter = int(os.environ.get('DELETE_IN_SECONDS', 30))
    while counter > 1:
        time.sleep(1)
        counter -= 1
        print('Deleting in %d seconds' % counter)
    client.files_delete_v2(filepath)
