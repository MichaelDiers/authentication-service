'''
    Tests for AuthService.
'''

from authentication.model.sign_in_request import SignInRequest
from authentication.model.sign_up_request import SignUpRequest
from authentication.service.auth_service import AuthService
from authentication.service.jwt_service import JwtService


def test_empty_init() -> None:
    '''
        Test for empty __init__.
    '''
    service = AuthService()
    assert service.jwt_service is not None


def test_init() -> None:
    '''
        Test for __init__.
    '''
    jwt_service = JwtService('RS256', 'my secret')
    service = AuthService(jwt_service)
    assert service.jwt_service is not None


def test_sign_in() -> None:
    '''
        Test for sign_in.
    '''
    sign_in_request = SignInRequest('email', 'password')
    service = AuthService()
    token_response, status = service.sign_in(sign_in_request)
    assert token_response is not None
    assert token_response.token is not None
    assert len(token_response.token.split('.')) == 3
    assert status == 200


def test_sign_up() -> None:
    '''
        Test for sign_up.
    '''
    sign_up_request = SignUpRequest('display name', 'email', 'password')
    service = AuthService()
    token_response, status = service.sign_up(sign_up_request)
    assert token_response is not None
    assert token_response.token is not None
    assert len(token_response.token.split('.')) == 3
    assert status == 201
