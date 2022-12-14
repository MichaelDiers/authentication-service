'''
    Service for authentication operations.
'''
from typing import Tuple
from authentication.model.payload import Payload
from authentication.model.token_response import TokenResponse


class AuthService:
    '''
        Service for authenticating users.
    '''

    def __init__(self, user_service, jwt_service) -> None:
        '''
            Create a new instance of AuthService.

            Args:
                user_service: Service for reading and creating users.
                jwt_service (JwtService): Service for creating json web tokens.
        '''
        self.jwt_service = jwt_service
        self.user_service = user_service

    def health(self) -> Tuple[dict, int]:
        '''
            A health check for the service.

            Returns:
                dict: A dictionary containing the result of the health check.
        '''
        users_result, _ = self.user_service.health()
        users_result['info']['Authentication Service'] = {'status': 'up'}
        users_result['details']['Authentication Service'] = {'status': 'up'}
        return users_result, 200

    def sign_in(self, sign_in_request) -> Tuple[TokenResponse, int]:
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
        user, status = self.user_service.read(sign_in_request)
        if not user:
            return None, status

        token_response = self.jwt_service.encode(Payload(user.display_name))
        return token_response, 200

    def sign_up(self, sign_up_request) -> Tuple[TokenResponse, int]:
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
        user, status = self.user_service.create(sign_up_request)
        if not user:
            return None, status

        token_response = self.jwt_service.encode(Payload(user.display_name))
        return token_response, 201
