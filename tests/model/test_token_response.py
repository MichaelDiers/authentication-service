'''
    Tests for TokenResponse.
'''
from authentication.model.token_response import TokenResponse


def test_init():
    '''
        Test the initialization.
    '''
    token = 'my token'

    response = TokenResponse(token)

    assert token == response.token
