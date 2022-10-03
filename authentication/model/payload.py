'''
    Describes the payload of a json web token.
'''


class Payload:
    '''
         Describes the payload of a json web token.
     '''

    def __init__(self, display_name) -> None:
        '''
            Create a new Payload.

            Args:
                display_name (string): The display name of the user.
        '''
        self.display_name = display_name

    def to_dict(self) -> dict:
        '''
            Generate a dictionary from all fields.

            Returns:
                dict: A dictionary containing all fields.
        '''
        return {
            'displayName': self.display_name
        }
