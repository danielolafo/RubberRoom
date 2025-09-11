

def page_to_list(page):
    list = []
    for item in page:
        list.append(item)
    return list

class ValidationResponse:
    def __init__(self):
        self.is_valid=False
        self.message=''

    def __init__(self, is_valid, message):
        self.is_valid = is_valid
        self.message = message

    class ValidationResponseBuilder:

        def __init__(self):
            self.is_valid=None
            self.message=None
        def build_valid(self, is_valid):
            self.is_valid=is_valid
            return self

        def build_message(self, message):
            self.message = message
            return self

        def build(self):
            return ValidationResponse()
            #return ValidationResponse(self.is_valid, self.message)

class ValidationResponseBuilder:

    def __init__(self):
        self.is_valid=None
        self.message=None
    def build_valid(self, is_valid):
        self.is_valid=is_valid
        return self

    def build_message(self, message):
        self.message = message
        return self

    def build(self):
        return ValidationResponse(self.is_valid, self.message)

class Constants:
    PHOTOS = 'photos'
    ALLOCATION_ID = 'allocation_id'