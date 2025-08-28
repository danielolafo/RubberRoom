from django.db import models

"""
Define the priority that a owner wants to give to their location.
If the user wants to give a high priority to one category over another It will give a 1  max - 10 min
category score for appears in the filter when users looking for a specific temporal residence category
"""
class CategoryPriority(models.Model):

    def __init__(self, category):
        self.allocationSite = None
        self.category = category
        self.priority = None