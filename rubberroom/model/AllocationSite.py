from django.db import models

class AllocationSite(models.Model):

    def __init__(self):
        self.city = None
        self.address = None
        self.owner = None
        self.ratings = []
        self.tags = []