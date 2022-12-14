'''
    Service for creating json web tokens.
'''
import jwt
from authentication.model.token_response import TokenResponse

# pylint: disable=too-few-public-methods


class JwtService:
    '''
        Service for creating json web tokens.
    '''

    def __init__(self, algorithm, secret) -> None:
        '''
            Create a new JwtService.

            Args:
                algorithm (str): The algorithm used for jwt creation.
                secret (str): The secret used for jwt creation.
        '''
        self.algorithm = algorithm
        self.secret = secret

    def encode(self, payload) -> TokenResponse:
        '''
            Create a json web token by using the given payload.

            Args:
                payload (Payload): The payload of the token.

            Returns:
                TokenResponse: A response object that contains the token.
        '''
        token = jwt.encode(
            payload.to_dict(),
            self.secret,
            algorithm=self.algorithm
        )

        return TokenResponse(token)
