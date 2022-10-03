'''
    Service for authentication operations.
'''
from authentication.model.payload import Payload
from authentication.model.token_response import TokenResponse
from authentication.service.jwt_service import JwtService


class AuthService:
    '''
        Service for authenticating users.
    '''

    def __init__(self, jwt_service=JwtService()) -> None:
        '''
            Create a new instance of AuthService.

            Args:
                jwt_service (JwtService, optional): Service for creating json web tokens.
                    Defaults to JwtService().
        '''
        self.jwt_service = jwt_service

    def sign_in(self, sign_in_request) -> TokenResponse:
        '''
            Sign in the given user.

            Args:
                sign_in_request (SignInRequest): The request data.

            Returns:
                TokenReponse, int: The token response is set only for successful sign-ins.
                  TokenResponse, 200: Sign-in is successful.
                  None, 400: Sign-in failed due to invalid request.
                  None, 404: Unknown combination of user/email.
                  None, 500: Internal server error.
        '''
        display_name = 'display name'
        token_response = self.jwt_service.encode(Payload(display_name))
        return token_response, 200

    def sign_up(self, sign_up_request):
        '''
            Sign up a new user.

            Args:
                sign_up_request (SignUpRequest): The request data.

            Returns:
                TokenReponse, int: The token response is set only for successful sign-ups.
                  TokenResponse, 201: Sign-up is successful.
                  None, 400: Sign-up failed due to invalid request.
                  None, 409: User already exists.
                  None, 500: Internal server error.
        '''
        display_name = sign_up_request.display_name
        token_response = self.jwt_service.encode(Payload(display_name))
        return token_response, 201
