import json


class AllocationSiteDto:
    def __init__(self):
        self.city = None
        self.address = None
        # owner = models.ForeignKey(User, on_delete=models.PROTECT, null=True, default=None)
        self.ratings = []
        self.tags = []

"""
    def __dict__(self):
        print('Dict ', self.__dict__)
        return json.dumps(self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4)
"""