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

    def to_dict(self) -> dict:
        '''
            Generate a dictionary from all fields.

            Returns:
                dict: A dictionary containing all fields.
        '''
        return {'token': self.token}
