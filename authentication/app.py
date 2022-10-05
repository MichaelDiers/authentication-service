'''
    Authentication api using flask.
'''
from flask import Flask
from marshmallow import exceptions
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

    @app.errorhandler(404)
    def handle_not_found(_):
        return {}, 404

    @app.errorhandler(Exception)
    def handle_all_errors(_):
        return {}, 500

    app.register_blueprint(sign_in_route)
    app.register_blueprint(sign_up_route)

    return app
