'''
    The base configuration of the application.
'''

# pylint: disable=too-few-public-methods

from authentication.config.config import Config


class ProductionConfig(Config):
    '''
        The base configuration of the application.
    '''
    TESTING = False
