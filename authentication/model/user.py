'''
    Describes a user.
'''

# pylint: disable=too-few-public-methods


class User:
    '''
        Describes a user.
    '''

    def __init__(self, display_name, guid):
        '''
            Create a new instance of User.

            Args:
                display_name (str): The display name of the user.
                guid (str): The id of the user.
        '''
        self.display_name = display_name
        self.guid = guid

    def __str__(self):
        '''
            Create a string representation of the object.

            Returns:
                str: The string representation.
        '''
        return f'{User.__name__}: (display_name: {self.display_name}, guid: {self.guid})'
