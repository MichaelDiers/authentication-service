'''
    Describes the schema of a sign in request.
'''
from marshmallow import fields, post_load, RAISE, Schema, validate
from authentication.model.sign_in_request import SignInRequest


class SignInRequestSchema(Schema):
    '''
        Describes the schema of a sign in request thats extends Schema.
    '''
    class Meta:
        '''
            Defines the metadata of the schema.
        '''
        unknown = RAISE  # raise an exception for undefined properties

    email = fields.Email(
        required=True,
        validate=validate.Length(min=5, max=2048)
    )
    password = fields.String(
        required=True,
        validate=validate.Length(min=8, max=4096)
    )

    @post_load
    def create_sign_in_request(self, data, **kwargs):  # pylint: disable=unused-argument
        '''
            Transform the data to a SignInRequest
        '''
        return SignInRequest(**data)
