'''
    Describes the schema of a sign in request.
'''
from marshmallow import fields, validate
from authentication.model.sign_up_request import SignUpRequest
from authentication.schema.sign_in_request_schema import SignInRequestSchema


class SignUpRequestSchema(SignInRequestSchema):
    '''
        Describes the schema of a sign up request thats extends the sign in schema.
    '''

    __model__ = SignUpRequest

    display_name = fields.String(
        data_key='displayName',
        required=True,
        validate=validate.Length(min=3, max=256)
    )
