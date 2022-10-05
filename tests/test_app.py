'''
    Tests for app.
'''
from unittest.mock import Mock, patch
import pytest
from authentication.model.sign_in_request import SignInRequest
from authentication.model.sign_up_request import SignUpRequest
from tests.test_config import TestConfig


@pytest.fixture(
    params=[
        # success
        (200, 200, lambda: {
         'displayName': 'display name', 'guid': 'a guid'}, None, TestConfig.API_KEY),
        # user not found
        (404, 404, lambda: {}, None, TestConfig.API_KEY),
        # invalid response
        (200, 404, lambda: {}, None, TestConfig.API_KEY),
        # exception at service call
        (200, 500, lambda: 1/0, None, TestConfig.API_KEY),
        # empty input json
        (200, 400, lambda: 1/0, {}, TestConfig.API_KEY),
        # missing api key
        (404, 403, lambda: {}, {}, ''),
        # invalid api key
        (404, 403, lambda: {}, {}, 'A WRONG API KEY')
    ]
)
def client_sign_in(client, request):
    '''
        Create test data for sign in tests.

        Args:
            client (TestClient): A flask test client.
            request: A special fixture parameter.

        Returns:
            Tuple: A tuple containing the test data.
    '''
    return (client, ) + request.param


@pytest.fixture(
    params=[
        # create succeeds
        (201, 201, lambda: {
         'displayName': 'the display name', 'guid': 'a new guid'}, None, TestConfig.API_KEY),
        # user already exists
        (409, 409, lambda: {}, None, TestConfig.API_KEY),
        # invalid response from mock
        (201, 404, lambda: {}, None, TestConfig.API_KEY),
        # raise service error
        (201, 500, lambda: 1/0, None, TestConfig.API_KEY),
        # empty input json
        (201, 400, lambda: 1/0, {}, TestConfig.API_KEY),
        # missing api key
        (404, 403, lambda: {}, {}, ''),
        # invalid api key
        (404, 403, lambda: {}, {}, 'A WRONG API KEY')
    ]
)
def client_sign_up(client, request):
    '''
        Create test data for sign up tests.

        Args:
            client (TestClient): A flask test client.
            request: A special fixture parameter.

        Returns:
            Tuple: A tuple containing the test data.
    '''
    return (client, ) + request.param


def test_sign_in(client_sign_in) -> None:  # pylint: disable=redefined-outer-name
    '''
        Test for signing in a user.

        Args:
            client_sign_in (Tuple): The test data.
    '''
    client, status_code_mock, status_code_service, json, request, api_key = client_sign_in
    sign_in_request = request if request is not None else SignInRequest(
        'email@example.com',
        'my password').to_dict()

    with patch('requests.post') as mock:
        mock.return_value = Mock(
            status_code=status_code_mock,
            json=json
        )

        response = client.post(
            '/sign-in',
            json=sign_in_request,
            headers={'x-api-key': api_key}
        )
        assert response.status_code == status_code_service
        if status_code_service in [400, 403]:
            mock.assert_not_called()
        else:
            mock.assert_called_once()

        if status_code_service == 200:
            assert 'token' in response.json
            token = response.json['token']
            assert token is not None
            assert len(token.split('.')) == 3
        else:
            assert len(response.json) == 0


def test_sign_up(client_sign_up) -> None:  # pylint: disable=redefined-outer-name
    '''
        Test for signing up a user.

        Args:
            client_sign_up (Tuple): The test data.
    '''
    client, status_code_mock, status_code_service, json, request, api_key = client_sign_up
    sign_up_request = request if request is not None else SignUpRequest(
        'display name',
        'email@example.com',
        'my password').to_dict()

    with patch('requests.post') as mock:
        mock.return_value = Mock(
            status_code=status_code_mock,
            json=json
        )

        response = client.post(
            '/sign-up',
            json=sign_up_request,
            headers={'x-api-key': api_key}
        )
        assert response.status_code == status_code_service
        if status_code_service in [400, 403]:
            mock.assert_not_called()
        else:
            mock.assert_called_once()

        if status_code_service == 201:
            assert 'token' in response.json
            token = response.json['token']
            assert token is not None
            assert len(token.split('.')) == 3
        else:
            assert len(response.json) == 0
