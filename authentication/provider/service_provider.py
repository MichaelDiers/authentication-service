'''
    Provider for services.
'''
from authentication.service.auth_service import AuthService
from authentication.service.jwt_service import JwtService
from authentication.service.user_service import UserService


class ServiceProvider:
    '''
        Provider for services.
    '''

    def __init__(self, config) -> None:
        '''
            Create a new instance of ServiceProvider.

            Args:
                config (dict): The flask app configuration.
        '''
        self.config = config

    def auth_service(self) -> AuthService:
        '''
            Initialize a new AuthService.

            Returns:
                AuthService: The authentication service.
        '''
        return AuthService(self.user_service(), self.jwt_service())

    def jwt_service(self) -> JwtService:
        '''
            Initialize a new JwtService.

            Returns:
                JwtService: The json web token service.
        '''
        algorithm = self.config['JWT_ALGORITHM']
        secret = self.config['JWT_SECRET']
        return JwtService(algorithm, secret)

    def user_service(self) -> UserService:
        '''
            Initialize a new UserService.

            Returns:
                UserService: The user service.
        '''
        url = self.config['USER_SERVICE_URL']
        return UserService(url)
