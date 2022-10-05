'''
    Authentication api using flask.
'''
from flask import Flask
from marshmallow import exceptions
from werkzeug.exceptions import HTTPException
from authentication.route.health_route import health_route
from authentication.route.sign_in_route import sign_in_route
from authentication.route.sign_up_route import sign_up_route
from authentication.config.production_config import ProductionConfig
from authentication.config.local_config import LocalConfig


def create_app(config=None) -> Flask:
    '''
        A fask application factory.

        Returns:
            Flask: A flask application.
    '''

    app = Flask(__name__)
    if config:
        app.config.from_object(config)
    else:
        prod_config = ProductionConfig()
        if prod_config.API_KEY is not None:
            app.config.from_object(prod_config)
        else:
            app.config.from_object(LocalConfig())

    @app.errorhandler(exceptions.ValidationError)
    def handle_validation_error(_):
        '''
            Handle validation errors.

            Args:
                _ (object): Ignored.

            Returns:
                str, int: An empty response and a status code.
        '''
        return {}, 400

    @app.errorhandler(HTTPException)
    def handle_http_exception(err):
        return {}, err.code

    @app.errorhandler(Exception)
    def handle_all_errors(err):
        print(err)
        return {}, 500

    app.register_blueprint(sign_in_route)
    app.register_blueprint(sign_up_route)
    app.register_blueprint(health_route)

    return app
