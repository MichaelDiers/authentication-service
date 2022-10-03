'''
    The sign-in route.
'''
from flask import Blueprint, jsonify, request
from authentication.schema.sign_in_request_schema import SignInRequestSchema
from authentication.service.auth_service import AuthService

sign_in_route = Blueprint('sign-in', __name__)


@sign_in_route.route("/sign-in", methods=['POST'])
def sign_in():
    '''
        Sign in the given user.

        Returns:
            TokenReponse, int: A tuple of TokenResponse and response status.
    '''
    sign_in_request = SignInRequestSchema().load(request.get_json())
    token_response, status = AuthService().sign_in(sign_in_request)
    json = jsonify(token_response.to_dict())
    return json, status
