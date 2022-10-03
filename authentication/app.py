'''
    Authentication api using flask.
'''
from flask import Flask, jsonify, request
from marshmallow import exceptions
from authentication.service.auth_service import AuthService
from authentication.schema.sign_in_request_schema import SignInRequestSchema
from authentication.schema.sign_up_request_schema import SignUpRequestSchema


def create_app() -> Flask:
    '''
        A fask application factory.

        Returns:
            Flask: A flask application.
    '''

    app = Flask(__name__)

    auth_service = AuthService()

    @app.errorhandler(exceptions.ValidationError)
    def handle_validation_error(_):
        return '', 400

    @app.route("/sign-in", methods=['POST'])
    def sign_in():
        '''
            Sign in the given user.

            Returns:
                TokenReponse, int: A tuple of TokenResponse and response status.
        '''
        sign_in_request = SignInRequestSchema().load(request.get_json())
        token_response, status = auth_service.sign_in(sign_in_request)
        json = jsonify(token_response.to_dict())
        return json, status

    @app.route("/sign-up", methods=['POST'])
    def sign_up():
        '''
            Sign up a new user.

            Returns:
                TokenReponse, int: A tuple of TokenResponse and response status.
        '''
        sign_up_request = SignUpRequestSchema().load(request.get_json())
        token_response, status = auth_service.sign_up(sign_up_request)
        json = jsonify(token_response.to_dict())
        return json, status

    return app
