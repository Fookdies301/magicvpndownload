"""
    Contains configuration for email notification
"""

import os
import smtplib
import logging as log
from flask_limiter.util import get_remote_address

EMAIL_SENDER_ID = os.environ.get('EMAIL_ADDRESS')
EMAIL_SENDER_PASSWORD = os.environ.get('EMAIL_PASSWORD')
EMAIL_RECEIVER_ID = os.environ.get('RECEIVE_EMAIL_ADDRESS')
APP_NAME = os.environ.get('APP_NAME', 'Magic VPN Server')


def send_email(message, ip=get_remote_address(), subject=APP_NAME + ' used'):

    body = f'''
{message}\n\nFrom: {ip}
    '''
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (EMAIL_SENDER_ID, EMAIL_RECEIVER_ID, subject, body)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(EMAIL_SENDER_ID, EMAIL_SENDER_PASSWORD)
        server.sendmail(EMAIL_SENDER_ID, EMAIL_RECEIVER_ID, message)
        server.close()
        log.info('Successfully sent the mail')
    except Exception as e:
        log.error(str(e))
        log.error('Failed to send mail..')


if __name__ == '__main__':
    send_email(message='some message', ip_address='127.0.0.1')
