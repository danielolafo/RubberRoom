from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    state = models.CharField(max_length=1, default=1)

    class Meta:
        db_table = 'category'

"""
Define the priority that a owner wants to give to their location.
If the user wants to give a high priority to one category over another It will give a 1  max - 10 min
category score for appears in the filter when users looking for a specific temporal residence category
"""
class CategoryPriority(models.Model):
    #allocationSite = models.ForeignKey(AllocationSite)
    #category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, default=None)
    priority = models.IntegerField(default=0)

    class Meta:
        db_table = 'category_priority'


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, null=True, blank=True)
    user_rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    description = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(max_length=40, null=False, blank=False, default='*')

    class Meta:
        db_table = 'users'

class AllocationSite(models.Model):
    city = models.CharField(max_length=150, null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    #owner = models.ForeignKey(User, on_delete=models.PROTECT, null=True, default=None)
    ratings=[]
    tags=[]

    class Meta:
        db_table = 'allocation_site'

class MediaData(models.Model):
    #allocation_site = models.ForeignKey(AllocationSite, on_delete=models.PROTECT, null=True, default=None)
    photos=[]
    video=[]

"""
The rating asigned to an allocation by an user.
"""
class Rating(models.Model):
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    comment = models.CharField(max_length=150, null=True, blank=True)
    #user=models.ForeignKey(User,  on_delete=models.PROTECT, null=True, default=None)
    #allocation=models.ForeignKey(AllocationSite, on_delete=models.PROTECT, null=True, default=None)

    class Meta:
        db_table = 'rating'