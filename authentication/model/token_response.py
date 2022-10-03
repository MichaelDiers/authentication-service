'''
    Describes a token response.
'''


class TokenResponse:
    '''
        Describes a token response.
    '''

    def __init__(self, token) -> None:
        '''
            Creates a new TokenResponse.

            Args:
                token (string): A json web token.
        '''
        self.token = token
