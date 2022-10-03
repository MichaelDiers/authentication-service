'''
    Tests for app.
'''
from tests.schema.test_sign_in_request_schema import create_payload as create_sign_in_request
from tests.schema.test_sign_up_request_schema import create_payload as create_sign_up_request


def test_sign_in_fails_with_empty_json(client) -> None:
    '''
        Test for sign_in (fail).
    '''
    payload = create_sign_in_request(None, None)
    response = client.post("/sign-in", json=payload)
    assert response.status_code == 400


def test_sign_in_succeeds(client) -> None:
    '''
        Test for sign_in (success).
    '''
    payload = create_sign_in_request()
    response = client.post("/sign-in", json=payload)
    assert response.status_code == 200
    token = response.json["token"]
    assert token is not None
    assert len(token.split('.')) == 3


def test_sign_up_fails_with_empty_json(client) -> None:
    '''
        Test for sign_up (fail).
    '''
    payload = create_sign_up_request(None, None, None)
    response = client.post("/sign-up", json=payload)
    assert response.status_code == 400


def test_sign_up_succeeds(client) -> None:
    '''
        Test for sign_up (success).
    '''
    payload = create_sign_up_request()
    response = client.post("/sign-up", json=payload)
    assert response.status_code == 201
    token = response.json["token"]
    assert token is not None
    assert len(token.split('.')) == 3
