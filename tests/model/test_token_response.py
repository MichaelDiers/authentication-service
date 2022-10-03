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


def test_to_dict():
    '''
        Test for to_dict.
    '''
    token = 'token'
    token_response = TokenResponse(token)
    dictionary = token_response.to_dict()
    assert dictionary is not None
    assert len(dictionary) == 1
    assert dictionary['token'] == token


def test_str():
    '''
        Test for __str__.
    '''
    response = TokenResponse('tok.e.n')
    expected = 'TokenResponse: (token: tok.e.n)'
    assert expected == str(response)
