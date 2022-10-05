'''
    The base configuration of the application.
'''

# pylint: disable=too-few-public-methods

from authentication.config.config import Config


class LocalConfig(Config):
    '''
        The local configuration of the application.
    '''
    API_KEY = 'API_KEY'
    JWT_ALGORITHM = 'HS256'
    JWT_SECRET = 'secret'
    TESTING = True
    USER_SERVICE_URL = 'https://api-gateway-prdsggicqa-uc.a.run.app/api/v1/users-service'
