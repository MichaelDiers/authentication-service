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


def test_to_dict():
    '''
        Test for creating a dictionary from the payload data.
    '''
    display_name = 'my display name'
    expected_key = 'displayName'
    payload = Payload(display_name)
    dictionary = payload.to_dict()
    assert display_name == dictionary[expected_key]
    assert len(dictionary) == 1


def test_str():
    '''
        Test for __str__.
    '''
    payload = Payload('display name')
    expected = 'Payload: (displayName: display name)'
    assert expected == str(payload)
