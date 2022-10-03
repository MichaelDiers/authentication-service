'''
    Tests for JwtService.
'''

from authentication.service.jwt_service import JwtService
from authentication.model.payload import Payload


def test_empty_init() -> None:
    '''
        Test for empty __init__.
    '''
    service = JwtService()
    assert service.algorithm == 'HS256'
    assert service.secret == 'secret'


def test_init() -> None:
    '''
        Test for __init__.
    '''
    service = JwtService('RS256', 'my secret')
    assert service.algorithm == 'RS256'
    assert service.secret == 'my secret'


def test_encode() -> None:
    '''
        Test for encode.
    '''
    display_name = 'my display name'
    payload = Payload(display_name)
    service = JwtService()
    token_response = service.encode(payload)
    assert token_response is not None
    assert token_response.token is not None
    assert len(token_response.token.split('.')) == 3
