import os

MAX_SIZE_IN_MB = os.environ.get('MAX_DOWNLOAD_SIZE', 10)


def max_file_size_in_byte():
    return MAX_SIZE_IN_MB * 1024 * 1024


def max_file_size_in_mb():
    return MAX_SIZE_IN_MB
