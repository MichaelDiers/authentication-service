'''
    Tests for TokenResponse.
'''
from authentication.model.user import User


def test_init():
    '''
        Test the initialization.
    '''
    display_name = 'my display name'

    user = User(display_name)

    assert user.display_name == display_name


def test_str():
    '''
        Test for __str__.
    '''
    user = User('my display name')
    expected = 'User: (display_name: my display name)'
    assert expected == str(user)
