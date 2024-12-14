'''
Logging helpers

Maintainer: Sparsh Bamrara
'''
import os
import logging

logger = logging.getLogger(name='CG Scripts')

LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')

logging.basicConfig(
    format='[ %(levelname)s ] %(asctime)s - %(message)s',
    level=logging.getLevelName(level=LOG_LEVEL)
)


class LogColors:
    '''
    ANSI color codings for logging colors
    '''
    HEADER = '\033[95m'
    OK_BLUE = '\033[94m'
    OK_CYAN = '\033[96m'
    OK_GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class ColorLogger:
    '''
    Color logged lines
    '''
    def __init__(self, name: str=''):
        self.logger = logging.getLogger(name)

        logging.basicConfig(
            format='%(asctime)s - %(message)s',
            level=logging.getLevelName(logging.INFO)
        )

    def info(self, _s: str):
        '''
        Info logger
        '''
        self.logger.info('%s%s%s', LogColors.OK_BLUE, _s, LogColors.END)

    def success(self, _s: str):
        '''
        Success logger
        '''
        self.logger.info('%s%s%s', LogColors.OK_GREEN, _s, LogColors.END)

    def warning(self, _s: str):
        '''
        Warning logger
        '''
        self.logger.info('%s%s%s', LogColors.WARNING, _s, LogColors.END)

    def error(self, _s: str):
        '''
        Error logger
        '''
        self.logger.info('%s%s%s', LogColors.FAIL, _s, LogColors.END)

    def header(self, _s: str):
        '''
        Header logger
        '''
        self.logger.info('%s%s%s', LogColors.HEADER, _s, LogColors.END)

    def bold(self, _s: str):
        '''
        Bold logger
        '''
        self.logger.info('%s%s%s', LogColors.BOLD, _s, LogColors.END)

    def underlined(self, _s: str):
        '''
        Underlined logger
        '''
        self.logger.info('%s%s%s', LogColors.UNDERLINE, _s, LogColors.END)
