'''
    The sign-up route.
'''
from flask import Blueprint, jsonify, request
from authentication.schema.sign_up_request_schema import SignUpRequestSchema
from authentication.service.auth_service import AuthService

sign_up_route = Blueprint('sign-up', __name__)


@sign_up_route.route("/sign-up", methods=['POST'])
def sign_up():
    '''
        Sign up a new user.

        Returns:
            TokenReponse, int: A tuple of TokenResponse and response status.
    '''
    sign_up_request = SignUpRequestSchema().load(request.get_json())
    token_response, status = AuthService().sign_up(sign_up_request)
    json = jsonify(token_response.to_dict() if token_response else {})
    return json, status
