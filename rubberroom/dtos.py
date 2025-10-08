import json

import pydantic
from pydantic import BaseModel

class AllocationSiteDto:
    def __init__(self):
        self.id = None
        self.city = None
        self.address = None
        self.owner = None
        self.ratings = []
        self.tags = []

class UserDto:
    def __init__(self):
        self.id = None
        self.username = None
        self.user_rating = None
        self.description = None
        self.email = None

class WrapperResponse():

    def __init__(self):
        self.data=None
        self.message=None
        self.success=None