'''
    The default configuration for testing.
'''

# pylint: disable=too-few-public-methods

from authentication.config.config import Config


class TestConfig(Config):
    '''
        The app configuration for testing.
    '''
    JWT_ALGORITHM = 'HS256'
    JWT_SECRET = 'test secret'
    TESTING = True
    USER_SERVICE_URL = 'to be mocked'
