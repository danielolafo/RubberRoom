from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, null=False, blank=True)
    state = models.CharField(max_length=1, default=1)

    class Meta:
        db_table = 'category'


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, null=False, blank=True, error_messages='The username is required')
    user_rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    description = models.CharField(max_length=150, null=False, blank=True)
    email = models.EmailField(max_length=40, null=False, blank=False, default='*')

    class Meta:
        db_table = 'users'

class AllocationSite(models.Model):
    city = models.CharField(max_length=150, null=False, blank=True)
    address = models.CharField(max_length=150, null=False, blank=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT, null=False, default=None, error_messages={'Error':'Please provide an owner for this allocation'})
    ratings=[]
    tags=[]

    class Meta:
        db_table = 'allocation_site'

"""
Define the priority that a owner wants to give to their location.
If the user wants to give a high priority to one category over another It will give a 1  max - 10 min
category score for appears in the filter when users looking for a specific temporal residence category
"""
class CategoryPriority(models.Model):
    allocationSite = models.ForeignKey(AllocationSite, on_delete=models.PROTECT, null=False, default=None)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=False, default=None)
    priority = models.IntegerField(default=0)

    class Meta:
        db_table = 'category_priority'

class MediaData(models.Model):
    id = models.BigAutoField(primary_key=True)
    allocation_id = models.ForeignKey(AllocationSite, on_delete=models.PROTECT, null=False, default=None)
    insert_date = models.DateField()
    state = models.CharField()
    content= models.BinaryField()

    class Meta:
        db_table = 'media_data'

"""
The rating asigned to an allocation by an user.
"""
class Rating(models.Model):
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    comment = models.CharField(max_length=150, null=False, blank=True)
    user=models.ForeignKey(User,  on_delete=models.PROTECT, null=False, default=None)
    allocation=models.ForeignKey(AllocationSite, on_delete=models.PROTECT, null=False, default=None)

    class Meta:
        db_table = 'rating'

class Tag(models.Model):
    description = models.CharField(max_length=100)
    state = models.CharField(max_length=1)
    creation_date = models.DateField()

    class Meta:
        db_table = 'tag'

class AllocationSiteTags(models.Model):
    allocation_site_id = models.ForeignKey(AllocationSite, on_delete=models.PROTECT, null=False, default=None)
    tag_id = models.ForeignKey(Tag, on_delete=models.PROTECT, null=False, default=None)