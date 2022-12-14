'''
    Tests for sign in request schema validation.
'''
from uuid import uuid4
import pytest
from authentication.schema.sign_in_request_schema import SignInRequestSchema

EMAIL = 'email'
EMAIL_NOT_VALID = 'Not a valid email address.'
EMAIL_LENGTH = 'Length must be between 5 and 2048.'

PASSWORD = 'password'
PASSWORD_LENGTH = 'Length must be between 8 and 4096.'

MISSING_DATA = 'Missing data for required field.'

VALID_EMAIL = 'example@example.com'
VALID_EMAIL_MAX = ''.join(
    ['a' for a in range(2048 - len(VALID_EMAIL))]) + VALID_EMAIL
VALID_PASSWORD = str(uuid4())
VALID_PASSWORD_MAX = ''.join('a' for x in range(4096))
VALID_PASSWORD_MIN = ''.join('a' for x in range(8))


def create_payload(email=VALID_EMAIL, password=VALID_PASSWORD):
    '''
        Create the payload for testing the schema.

        Args:
            email (string): The email address of a user.
            password (string): The passwordd of a user.
    '''
    data = {}
    if email:
        data['email'] = email

    if password:
        data['password'] = password

    return data


def check_for_errors(errors, expected_email, expected_password, additional_errors=0):
    '''
        Analyze the schema validation result.

        Args:
            errors (dict): A dictionary containing the results of the schema validation.
            expected_email (string): The expected email validation error or None.
            expected_password (string): The expected password validation error or None.
            additional_errors (int, optional): Set if additional errors are expected. Defaults to 0.

        Returns:
            int: The total number of errors without additional_errors
    '''
    error_count = 0
    if not expected_email:
        assert EMAIL not in errors
    else:
        assert EMAIL in errors
        assert expected_email in errors[EMAIL]
        error_count += 1

    if not expected_password:
        assert PASSWORD not in errors
    else:
        assert PASSWORD in errors
        assert expected_password in errors[PASSWORD]
        error_count += 1

    assert error_count + additional_errors == len(errors)
    return error_count


@pytest.mark.parametrize(
    'email,password,expected_email,expected_password',
    [
        # missing data
        (None, None, MISSING_DATA, MISSING_DATA),
        # missing email
        (None, VALID_PASSWORD, MISSING_DATA, None),
        # invalid email
        ('email@', VALID_PASSWORD, EMAIL_NOT_VALID, None),
        # email max length
        (VALID_EMAIL_MAX, VALID_PASSWORD, None, None),
        # email too long
        ('a' + VALID_EMAIL_MAX, VALID_PASSWORD, EMAIL_LENGTH, None),
        # password too short
        (VALID_EMAIL, VALID_PASSWORD_MIN[1:], None, PASSWORD_LENGTH),
        # password min length
        (VALID_EMAIL, VALID_PASSWORD_MIN, None, None),
        # password max length
        (VALID_EMAIL, VALID_PASSWORD_MAX, None, None),
        # password too long
        (VALID_EMAIL, VALID_PASSWORD_MAX + 'a', None, PASSWORD_LENGTH),
    ]
)
def test_validation(email, password, expected_email, expected_password):
    '''
        Test the schema validation for given email and password.

    Args:
        email (string): The input email.
        password (string): The input password.
        expected_email (string): The expected email validation error or None.
        expected_password (string): The expected password validation error or None.
    '''
    errors = SignInRequestSchema().validate(create_payload(email, password))
    check_for_errors(errors, expected_email, expected_password)


def test_for_additional_parameter_rejection():
    '''reject additional inputs'''
    payload = create_payload(VALID_EMAIL, VALID_PASSWORD)
    payload['foo'] = 'bar'
    errors = SignInRequestSchema().validate(payload)
    assert 'foo' in errors
    assert 'Unknown field.' in errors['foo']


def test_post_load() -> None:
    '''Test for post_load.'''
    payload = create_payload(VALID_EMAIL, VALID_PASSWORD)
    sign_in_request = SignInRequestSchema().load(payload)
    assert sign_in_request is not None
    assert sign_in_request.email == VALID_EMAIL
    assert sign_in_request.password == VALID_PASSWORD
