import os
import requests


def download_file(url, filename):
    """
        Downloads file from the url and save it as filename
    """
    # check if file already exists
    if os.path.isfile(filename):
        os.remove(filename)
    print('Downloading File')
    response = requests.get(url)
    # Check if the response is ok (200)
    if response.status_code == 200:
        # Open file and write the content
        file_abs_path = os.path.join('/app/downloads', filename)
        with open(file_abs_path, 'wb') as file:
            # A chunk of 128 bytes
            for chunk in response:
                file.write(chunk)
    print(os.listdir('.'))
    print("******")
    print(os.system('pwd'))
