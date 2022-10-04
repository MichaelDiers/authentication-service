'''
    Tests for sign_in_request.py
'''
from authentication.model.sign_in_request import SignInRequest


def test_init():
    '''
        Test the initialization.
    '''
    email = 'my email'
    password = 'my password'

    request = SignInRequest(email, password)

    assert email == request.email
    assert password == request.password


def test_str():
    '''
        Test for __str__.
    '''
    request = SignInRequest('email@example.com', 'my password')
    expected = 'SignInRequest: (email: email@example.com, password: my password)'
    assert expected == str(request)


def test_to_dict():
    '''
        Test for to_dict.
    '''
    email = 'email@example.com'
    password = 'my password'
    request = SignInRequest(email, password)
    dictionary = request.to_dict()
    assert len(dictionary) == 2
    assert dictionary['email'] == email
    assert dictionary['password'] == password
