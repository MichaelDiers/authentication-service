'''
    Access to the user rest service.
'''
from typing import Tuple
import requests
from authentication.model.user import User


class UserService:
    '''
        Access to the user rest service.
    '''

    def __init__(self, url):
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
        response = requests.post(
            f'{self.url}/create',
            sign_up_request.to_dict(),
            timeout=20
        )
        if response.status_code != 201:
            return None, response.status_code
        json = response.json()

        if 'displayName' in json and 'guid' in json:
            user = User(
                json['displayName'],
                json['guid']
            )
            return user, 201

        return None, 404

    def read(self, sign_in_request) -> Tuple[User, int]:
        '''
            Read a user by email.

            Args:
                sign_in_request (SignInRequest): A request that includes email and password.

            Returns:
                User, int: The found user or None and the http status code.
        '''
        response = requests.post(
            f'{self.url}/read',
            sign_in_request.to_dict(),
            timeout=20
        )
        if response.status_code != 200:
            return None, response.status_code
        json = response.json()

        if 'displayName' in json and 'guid' in json:
            user = User(
                json['displayName'],
                json['guid']
            )
            return user, 200

        return None, 404
