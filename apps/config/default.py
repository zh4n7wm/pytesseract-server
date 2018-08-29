# -*- coding: utf-8 -*-
import os

PROJECT_NAME = 'apps'
# SERVER_NAME = ''
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DEBUG = True
# os.urandom(24)
SECRET_KEY = b''
UPLOAD_FOLDER = '/tmp/'

# log
LOG_LEVEL = 'DEBUG'
LOG_DIR = '/tmp/'
LOGGER_NAME = PROJECT_NAME
