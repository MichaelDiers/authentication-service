'''
    The health route.
'''
from flask import Blueprint, current_app, jsonify, request
from authentication.schema.sign_up_request_schema import SignUpRequestSchema
from authentication.service.auth_service import AuthService
from authentication.provider.service_provider import ServiceProvider
from authentication.decorator.api_key import api_key

health_route = Blueprint('health', __name__)


@health_route.route('/health', methods=['GET'])
@api_key
def health():
    '''
        Execute a health check.

        Returns:
            dict, int: A tuple of dict and response status.
    '''
    auth_service = ServiceProvider(current_app.config).auth_service()
    response, status = auth_service.health()
    json = jsonify(response)
    return json, status
