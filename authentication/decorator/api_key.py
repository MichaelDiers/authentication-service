'''
    Describes an api key decorator.
'''
from functools import wraps
from flask import current_app, jsonify, request


def api_key(func):
    '''
        Decorator for checking a required api key.

        Args:
            f (Callable): The function that is called if the api check succeeds.

        Returns:
            Callable: The wrapper function.
    '''
    @wraps(func)
    def wrapper(*args, **kwds):
        expected_api_key = current_app.config['API_KEY']
        actual_api_key = request.headers.get('x-api-key')
        if expected_api_key == actual_api_key:
            return func(*args, **kwds)

        return jsonify({}), 403
    return wrapper
