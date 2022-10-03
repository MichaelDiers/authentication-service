'''
    Access to the user rest service.
'''

from typing import Tuple
from authentication.model.user import User


class UserService:
    '''
        Access to the user rest service.
    '''

    def __init__(self, url='url'):
        '''
            Create a new instance of UserService.

            Args:
                url (str): The base address of the user service.
        '''
        self.url = url

    def create(self, sign_up_request) -> Tuple[User, int]:
        '''
            Create a new user.

            Args:
                sign_up_request (SignUpRequest): The sign up data.

            Returns:
                User, int: The created user or None and the http status code.
        '''
        return User(sign_up_request.display_name), 201

    def read(self, email) -> Tuple[User, int]:
        '''
            Read a user by email.

            Args:
                email (str): The email of a user.

            Returns:
                User, int: The found user or None and the http status code.
        '''
        return User(email), 200
