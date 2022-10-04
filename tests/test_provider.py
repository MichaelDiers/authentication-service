'''
    Provider for test services.
'''
from authentication.service.auth_service import AuthService
from authentication.service.jwt_service import JwtService
from authentication.service.user_service import UserService
from tests.test_config import TestConfig

test_config = TestConfig()


def auth_service() -> AuthService:
    '''
        Create an auth service.

        Returns:
            AuthService: An auth service instance.
    '''
    return AuthService(user_service(), jwt_service())


def jwt_service() -> JwtService:
    '''
        Create a jwt service.

        Returns:
            JwtService: A jwt service instance.
    '''
    return JwtService(test_config.JWT_ALGORITHM, test_config.JWT_SECRET)


def user_service() -> UserService:
    '''
        Create an user service.

        Returns:
            UserService: An user service instance.
    '''
    return UserService(test_config.USER_SERVICE_URL)
