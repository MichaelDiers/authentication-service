'''
    Tests for UserService.
'''
from unittest.mock import Mock, patch
import pytest
from authentication.service.user_service import UserService
from authentication.model.sign_in_request import SignInRequest
from authentication.model.sign_up_request import SignUpRequest


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
def test_create(status_code_mock, status_code_service, json) -> None:
    '''
        Test for creating a new user.

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
        service = UserService('url')

        try:
            user, status = service.create(sign_up_request)

            mock.assert_called_once()
            assert status == status_code_service
            if status_code_service == 201:
                assert user is not None
                assert user.display_name == json()['displayName']
                assert user.guid == json()['guid']
            else:
                assert user is None
        except ZeroDivisionError:
            assert status_code_service == 500


def test_init() -> None:
    '''
        Test for __init__.
    '''
    service = UserService('url')
    assert service.url == 'url'


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
def test_read(status_code_mock, status_code_service, json) -> None:
    '''
        Test for reading a user.

        Args:
            status_code_mock (int): The status code of the called rest service mock.
            status_code_service (int): The expected status code of the user service call.
            json (lambda): A lambda that returns the json result of the rest service mock.
    '''
    sign_in_request = SignInRequest(
        'email@example.com',
        'my password'
    )

    with patch('requests.get') as mock:
        mock.return_value = Mock(
            status_code=status_code_mock,
            json=json
        )
        service = UserService('url')

        try:
            user, status = service.read(sign_in_request)

            mock.assert_called_once()
            assert status == status_code_service
            if status == 200:
                assert user is not None
                assert user.display_name == json()['displayName']
                assert user.guid == json()['guid']
            else:
                assert user is None
        except ZeroDivisionError:
            assert status_code_service == 500
