'''
User authentication controllers
'''
import os
from dotenv import load_dotenv
from fastapi import Request
from utils.logger import logger

load_dotenv()

def authenticated_user(request: Request) -> bool:
    '''
    Apply authentication on request
    '''
    token = request.headers.get('x-api-key')
    if not token or token != os.environ.get('API_KEY'):
        return False

    return True
