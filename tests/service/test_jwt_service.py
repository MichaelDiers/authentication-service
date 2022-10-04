'''
    Tests for JwtService.
'''

from authentication.model.payload import Payload
from tests.test_provider import jwt_service
from tests.test_config import TestConfig


def test_init() -> None:
    '''
        Test for __init__.
    '''
    service = jwt_service()
    assert service.algorithm == TestConfig.JWT_ALGORITHM
    assert service.secret == TestConfig.JWT_SECRET


def test_encode() -> None:
    '''
        Test for encode.
    '''
    display_name = 'my display name'
    payload = Payload(display_name)
    service = jwt_service()
    token_response = service.encode(payload)
    assert token_response is not None
    assert token_response.token is not None
    assert len(token_response.token.split('.')) == 3
