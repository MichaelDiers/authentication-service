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


@pytest.mark.parametrize(
    'email,password,expected_email,expected_password',
    [
        (None, None, MISSING_DATA, MISSING_DATA),  # missing data
        (None, VALID_PASSWORD, MISSING_DATA, None),  # missing email
        ('email@', VALID_PASSWORD, EMAIL_NOT_VALID, None),  # invalid email
        (VALID_EMAIL_MAX, VALID_PASSWORD, None, None),  # email max length
        ('a' + VALID_EMAIL_MAX, VALID_PASSWORD,
         EMAIL_LENGTH, None),  # email too long
        (VALID_EMAIL, 'aaaaaaa', None, PASSWORD_LENGTH),  # password too short
        (VALID_EMAIL, 'aaaaaaaa', None, None),  # password min length
        (VALID_EMAIL, VALID_PASSWORD_MAX, None, None),  # password max length
        (VALID_EMAIL, VALID_PASSWORD_MAX + 'a',
         None, PASSWORD_LENGTH),  # password too long
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
    if not expected_email:
        assert EMAIL not in errors
    else:
        assert EMAIL in errors
        assert expected_email in errors[EMAIL]

    if not expected_password:
        assert PASSWORD not in errors
    else:
        assert PASSWORD in errors
        assert expected_password in errors[PASSWORD]
