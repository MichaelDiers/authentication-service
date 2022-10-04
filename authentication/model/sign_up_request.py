'''
    Describes a sign up request.
'''

from authentication.model.sign_in_request import SignInRequest

# pylint: disable=too-few-public-methods


class SignUpRequest(SignInRequest):
    '''
        Describes a sign up request that extends SignInRequest.
    '''

    def __init__(self, display_name, email, password):
        '''
            Create a new SignUpRequest.

            Args:
                display_name (string): The display name of a user.
                email (string): The email address of a user.
                password (string): The password of a user.
        '''
        super().__init__(email, password)
        self.display_name = display_name

    def __str__(self):
        '''
            Create a string representation of the object.

            Returns:
                str: The string representation.
        '''
        data = super().__str__()
        data = data[:-1].replace(SignInRequest.__name__,
                                 SignUpRequest.__name__)
        return f'{data}, display_name: {self.display_name})'

    def to_dict(self) -> dict:
        '''
            Generate a dictionary from all fields.

            Returns:
                dict: A dictionary containing all fields.
        '''
        data = super().to_dict()
        data['displayName'] = self.display_name
        return data
