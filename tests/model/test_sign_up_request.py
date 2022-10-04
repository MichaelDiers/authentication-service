'''
    Tests for sign_up_request.py
'''
from authentication.model.sign_up_request import SignUpRequest


def test_init():
    '''
        Test the initialization.
    '''
    display_name = 'my display name'
    email = 'my email'
    password = 'my password'

    request = SignUpRequest(display_name, email, password)

    assert display_name == request.display_name
    assert email == request.email
    assert password == request.password


def test_str():
    '''
        Test for __str__.
    '''
    request = SignUpRequest('display name', 'email@example.com', 'my password')
    # pylint: disable-next=line-too-long
    expected = 'SignUpRequest: (email: email@example.com, password: my password, display_name: display name)'
    assert expected == str(request)


def test_to_dict():
    '''
        Test for to_dict.
    '''
    display_name = 'my display name'
    email = 'email@example.com'
    password = 'my password'
    request = SignUpRequest(display_name, email, password)
    dictionary = request.to_dict()
    assert len(dictionary) == 3
    assert dictionary['displayName'] == display_name
    assert dictionary['email'] == email
    assert dictionary['password'] == password
