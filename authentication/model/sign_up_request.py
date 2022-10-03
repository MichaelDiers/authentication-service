'''
    Describes a sign up request.
'''

from authentication.model.sign_in_request import SignInRequest


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
