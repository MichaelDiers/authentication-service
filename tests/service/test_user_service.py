'''
    Tests for UserService.
'''
from authentication.service.user_service import UserService


def test_init():
    '''
        Test for __init__.
    '''
    service = UserService('url')
    assert service.url == 'url'
