
class InvalidPageException(Exception):
    def __init__(self, message):
        self.message = message

class InvalidEmailException(Exception):
    def __init__(self, message):
        self.message = message