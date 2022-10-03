'''
    Tests for sign_up_request_schema.
'''
import pytest
from authentication.schema.sign_up_request_schema import SignUpRequestSchema
import tests.schema.test_sign_in_request_schema as sign_in

DISPLAY_NAME = 'displayName'
DISPLAY_NAME_LENGTH = 'Length must be between 3 and 256.'

VALID_DISPLAY_NAME = 'aaa'
VALID_DISPLAY_NAME_MAX = ''.join('a' for _ in range(256))
VALID_DISPLAY_NAME_MIN = ''.join('a' for _ in range(3))


def create_payload(
    display_name=VALID_DISPLAY_NAME,
    email=sign_in.VALID_EMAIL,
    password=sign_in.VALID_PASSWORD
):
    '''
        Create the payload for testing the schema.

        Args:
            display_name(string): The display name of the user.
            email (string): The email address of a user.
            password (string): The passwordd of a user.
    '''
    data = {}
    if display_name:
        data[DISPLAY_NAME] = display_name

    if email:
        data[sign_in.EMAIL] = email

    if password:
        data[sign_in.PASSWORD] = password

    return data


@pytest.mark.parametrize(
    'display_name,email,password,expected_display_name,expected_email,expected_password',
    [
        # missing data
        (None, None, None, sign_in.MISSING_DATA,
         sign_in.MISSING_DATA, sign_in.MISSING_DATA),
        # missing email
        (VALID_DISPLAY_NAME, None, sign_in.VALID_PASSWORD,
         None, sign_in.MISSING_DATA, None),
        # invalid email
        (VALID_DISPLAY_NAME, 'email@', sign_in.VALID_PASSWORD,
         None, sign_in.EMAIL_NOT_VALID, None),
        # email max length
        (VALID_DISPLAY_NAME, sign_in.VALID_EMAIL_MAX,
         sign_in.VALID_PASSWORD, None, None, None),
        # email too long
        (VALID_DISPLAY_NAME, 'a' + sign_in.VALID_EMAIL_MAX, sign_in.VALID_PASSWORD,
         None, sign_in.EMAIL_LENGTH, None),
        # password too short
        (VALID_DISPLAY_NAME, sign_in.VALID_EMAIL, sign_in.VALID_PASSWORD_MIN[1:],
         None, None, sign_in.PASSWORD_LENGTH),
        # password min length
        (VALID_DISPLAY_NAME, sign_in.VALID_EMAIL, sign_in.VALID_PASSWORD_MIN,
         None, None, None),
        # password max length
        (VALID_DISPLAY_NAME, sign_in.VALID_EMAIL, sign_in.VALID_PASSWORD_MAX,
         None, None, None),
        # password too long
        (VALID_DISPLAY_NAME, sign_in.VALID_EMAIL, sign_in.VALID_PASSWORD_MAX + 'a',
         None, None, sign_in.PASSWORD_LENGTH),
        # display name too short
        (VALID_DISPLAY_NAME_MIN[1:], sign_in.VALID_EMAIL, sign_in.VALID_PASSWORD,
         DISPLAY_NAME_LENGTH, None, None),
        # display name min length
        (VALID_DISPLAY_NAME_MIN, sign_in.VALID_EMAIL, sign_in.VALID_PASSWORD,
         None, None, None),
        # display name max length
        (VALID_DISPLAY_NAME_MAX, sign_in.VALID_EMAIL, sign_in.VALID_PASSWORD,
         None, None, None),
        # display name too long
        (VALID_DISPLAY_NAME_MAX + 'a', sign_in.VALID_EMAIL, sign_in.VALID_PASSWORD,
         DISPLAY_NAME_LENGTH, None, None),
    ]
)
def test_validation(  # pylint: disable=too-many-arguments
    display_name,
    email,
    password,
    expected_display_name,
    expected_email,
    expected_password
):
    '''
        Test the schema validation for given display_name, email and password.

    Args:
        display_name (string): The input display_name.
        email (string): The input email.
        password (string): The input password.
        expected_email (string): The expected email validation error or None.
        expected_password (string): The expected password validation error or None.
    '''
    errors = SignUpRequestSchema().validate(
        create_payload(display_name, email, password))
    error_count = sign_in.check_for_errors(
        errors,
        expected_email,
        expected_password,
        1 if expected_display_name else 0
    )

    if not expected_display_name:
        assert DISPLAY_NAME not in errors
    else:
        assert DISPLAY_NAME in errors
        assert expected_display_name in errors[DISPLAY_NAME]
        error_count += 1

    assert error_count == len(errors)


def test_for_additional_parameter_rejection():
    '''reject additional inputs'''
    payload = create_payload(
        VALID_DISPLAY_NAME, sign_in.VALID_EMAIL, sign_in.VALID_PASSWORD)
    payload['foo'] = 'bar'
    errors = SignUpRequestSchema().validate(payload)
    assert 'foo' in errors
    assert 'Unknown field.' in errors['foo']


def test_post_load() -> None:
    '''Test for post_load.'''
    payload = create_payload(
        VALID_DISPLAY_NAME, sign_in.VALID_EMAIL, sign_in.VALID_PASSWORD)
    sign_up_request = SignUpRequestSchema().load(payload)
    assert sign_up_request is not None
    assert sign_up_request.display_name == VALID_DISPLAY_NAME
    assert sign_up_request.email == sign_in.VALID_EMAIL
    assert sign_up_request.password == sign_in.VALID_PASSWORD
