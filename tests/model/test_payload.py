'''
    Tests for Payload.
'''
from authentication.model.payload import Payload


def test_init():
    '''
        Test the initialization.
    '''
    display_name = 'my display_name'

    payload = Payload(display_name)

    assert display_name == payload.display_name
