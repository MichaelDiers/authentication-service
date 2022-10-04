'''
    Tests for ServiceProvider
'''

from authentication.provider.service_provider import ServiceProvider

CONFIG = {
    'JWT_ALGORITHM': 'HS256',
    'JWT_SECRET': 'test secret',
    'TESTING': True,
    'USER_SERVICE_URL': 'to be mocked',
}


def test_init() -> None:
    '''
        Test __init__.
    '''
    provider = ServiceProvider(CONFIG)
    assert provider.config == CONFIG


def test_auth_service() -> None:
    '''
        Test for auth_service()
    '''
    provider = ServiceProvider(CONFIG)
    auth_service = provider.auth_service()
    assert auth_service is not None


def test_jwt_service() -> None:
    '''
        Test for jwt_service()
    '''
    provider = ServiceProvider(CONFIG)
    jwt_service = provider.jwt_service()
    assert jwt_service is not None


def test_user_service() -> None:
    '''
        Test for user_service()
    '''
    provider = ServiceProvider(CONFIG)
    user_service = provider.user_service()
    assert user_service is not None
