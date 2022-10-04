'''
    Tests for TokenResponse.
'''
from authentication.model.user import User


def test_init():
    '''
        Test the initialization.
    '''
    display_name = 'my display name'
    guid = 'the guid'

    user = User(display_name, guid)

    assert user.display_name == display_name
    assert user.guid == guid


def test_str():
    '''
        Test for __str__.
    '''
    user = User('my display name', 'the guid')
    expected = 'User: (display_name: my display name, guid: the guid)'
    assert expected == str(user)
