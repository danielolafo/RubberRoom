import json

import pydantic
from pydantic import BaseModel

class AllocationSiteDto:
    def __init__(self):
        self.city = None
        self.address = None
        # owner = models.ForeignKey(User, on_delete=models.PROTECT, null=True, default=None)
        self.ratings = []
        self.tags = []

class UserDto(pydantic.BaseModel):
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