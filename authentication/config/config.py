'''
    The base configuration of the application.
'''

# pylint: disable=too-few-public-methods


class Config:
    '''
        The base configuration of the application.
    '''
    API_KEY = None
    JWT_ALGORITHM = None
    JWT_SECRET = None
    TESTING = True
    USER_SERVICE_URL = None
