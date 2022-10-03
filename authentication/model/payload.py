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

    def __str__(self):
        '''
            Create a string representation of the object.

            Returns:
                str: The string representation.
        '''
        data = ', '.join(f'{key}: {value}' for (
            key, value) in self.to_dict().items())
        return f'{Payload.__name__}: ({data})'

    def to_dict(self) -> dict:
        '''
            Generate a dictionary from all fields.

            Returns:
                dict: A dictionary containing all fields.
        '''
        return {
            'displayName': self.display_name
        }
