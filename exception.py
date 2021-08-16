class Error(Exception):
    pass


class InputError(Error):
    """ If input of problems exceed 5"""

    def __init__(self):
        self.message = 'test'

    def __str__(self):
        return 'Error: Too many problems.'


class OperatorError(Error):
    """ If operator is not + or -"""

    def __init__(self):
        self.message = 'test'

    def __str__(self):
        return "Error: Operator must be '+' or '-'."


class DigitError(Error):
    """ If numbers contain characters other than digits"""

    def __init__(self):
        self.message = 'test'

    def __str__(self):
        return "Error: Numbers must only contain digits."


class LargeError(Error):
    """If inputted numbers are more than 4 digits"""

    def __init__(self):
        self.message = 'test'

    def __str__(self):
        return "Error: Numbers cannot be more than four digits."
