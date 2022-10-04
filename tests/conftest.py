'''
    Fixture for app tests.
'''
import pytest
from authentication.app import create_app
from tests.test_config import TestConfig


@pytest.fixture()
def app():
    '''
        Create a new app.

        Yields:
            Flask: A flask app.
    '''
    application = create_app(TestConfig())

    # other setup can go here

    yield application

    # clean up / reset resources here


@pytest.fixture()
def client(app):  # pylint: disable=redefined-outer-name
    '''
        Create a new client for testing.

        Args:
            app (Flask): A flask application.

        Returns:
            TestClient: A flask test client.
    '''
    return app.test_client()


@pytest.fixture()
def runner(app):  # pylint: disable=redefined-outer-name
    '''
        Create a flask cli runner.

        Args:
            app (Flask): A flask app.

        Returns:
            FlaskCliRunner: A flask cli runner.
    '''
    return app.test_cli_runner()
