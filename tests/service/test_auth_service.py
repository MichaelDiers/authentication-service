'''
    Tests for AuthService.
'''
# pylint: disable=duplicate-code
from unittest.mock import Mock, patch
import pytest
from authentication.model.sign_in_request import SignInRequest
from authentication.model.sign_up_request import SignUpRequest
from tests.test_provider import auth_service


def test_health() -> None:
    '''
        Test the health check.
    '''
    with patch('requests.get') as mock:
        mock.return_value = Mock(
            status_code=200,
            json=lambda: {
                'status': 'ok',
                'info': {},
                'error': {
                    'Users Service': {
                        'status': 'ok'
                    }
                },
                'details': {
                    'Users Service': {
                        'status': 'ok'
                    }
                }
            })
        service = auth_service()
        health, status = service.health()

        assert status == 200
        assert health['status'] == 'ok'


def test_health_failure() -> None:
    '''
        Test the health check for failure.
    '''
    with patch('requests.get') as mock:
        mock.return_value = Mock(
            status_code=200,
            json=lambda: {
                'status': 'error',
                'info': {},
                'error': {
                    'Users Service': {
                        'status': 'error'
                    }
                },
                'details': {
                    'Users Service': {
                        'status': 'error'
                    }
                }
            })
        service = auth_service()
        health, status = service.health()

        assert status == 200
        assert health['status'] == 'error'


def test_init() -> None:
    '''
        Test for __init__.
    '''
    service = auth_service()
    assert service.jwt_service is not None
    assert service.user_service is not None


@pytest.mark.parametrize(
    'status_code_mock,status_code_service,json',
    [
        # success
        (200, 200, lambda: {'displayName': 'display name', 'guid': 'a guid'}),
        # user not found
        (404, 404, lambda: {}),
        # invalid response
        (200, 404, lambda: {}),
        # exception at service call
        (200, 500, lambda: 1/0)
    ]
)
def test_sign_in(status_code_mock, status_code_service, json) -> None:
    '''
        Test for signing in a user.

        Args:
            status_code_mock (int): The status code of the called rest service mock.
            status_code_service (int): The expected status code of the user service call.
            json (lambda): A lambda that returns the json result of the rest service mock.
    '''
    sign_in_request = SignInRequest(
        'email@example.com',
        'my password'
    )

    with patch('requests.post') as mock:
        mock.return_value = Mock(
            status_code=status_code_mock,
            json=json
        )
        service = auth_service()

        try:
            token_response, status = service.sign_in(sign_in_request)

            mock.assert_called_once()
            assert status == status_code_service
            if status_code_service == 200:
                assert token_response is not None
                assert token_response.token is not None
                assert len(token_response.token.split('.')) == 3
            else:
                assert token_response is None

        except ZeroDivisionError:
            assert status_code_service == 500


@pytest.mark.parametrize(
    'status_code_mock,status_code_service,json',
    [
        # create succeeds
        (201, 201, lambda: {
         'displayName': 'the display name', 'guid': 'a new guid'}),
        # user already exists
        (409, 409, lambda: {}),
        # invalid response from mock
        (201, 404, lambda: {}),
        # raise service error
        (201, 500, lambda: 1/0)
    ]
)
def test_sign_up(status_code_mock, status_code_service, json) -> None:
    '''
        Test for signing up a new user.

        Args:
            status_code_mock (int): The status code of the called rest service mock.
            status_code_service (int): The expected status code of the user service call.
            json (lambda): A lambda that returns the json result of the rest service mock.
    '''
    sign_up_request = SignUpRequest(
        'display name',
        'email@example.com',
        'my password')

    with patch('requests.post') as mock:
        mock.return_value = Mock(
            status_code=status_code_mock,
            json=json
        )
        service = auth_service()

        try:
            token_response, status = service.sign_up(sign_up_request)

            mock.assert_called_once()
            assert status == status_code_service
            if status_code_service == 201:
                assert token_response is not None
                assert token_response.token is not None
                assert len(token_response.token.split('.')) == 3
            else:
                assert token_response is None
        except ZeroDivisionError:
            assert status_code_service == 500
