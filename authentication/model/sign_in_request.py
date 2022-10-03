'''
    Describes a request for signing in.
'''

# pylint: disable=too-few-public-methods


class SignInRequest:
    '''
        Describes a request for signing in.
    '''

    def __init__(self, email, password):
        '''
            Creates a new instance of SignInRequest.

            Args:
                email (string): The email of the user.
                password (string): The password of the user.
        '''
        self.email = email
        self.password = password

    def __str__(self):
        '''
            Create a string representation of the object.

            Returns:
                str: The string representation.
        '''
        return f'{SignInRequest.__name__}: (email: {self.email}, password: {self.password})'
