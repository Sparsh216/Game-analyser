'''
Application configs
'''
import os


class App:
    '''
    Application base configurations
    '''
    NAME = 'Game-data-analysing'
    VERSION = '0.1.0'

    DEBUG = os.environ.get('DEBUG', 'no') == 'no'
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
    STAGE = os.environ.get('STAGE', 'local')
