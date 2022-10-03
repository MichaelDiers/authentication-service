'''
    Describes a request for signing in.
'''


class SignInRequest(object):
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
