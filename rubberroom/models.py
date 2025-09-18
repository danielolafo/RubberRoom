from django.db import models
from django.core.validators import MinValueValidator

BASE_STATUS = [('A', 'Active'), ('I', 'Inactive')]
class Category(models.Model):
    name = models.CharField(max_length=150, null=False, blank=True)
    state = models.CharField(max_length=1, default=1)

    class Meta:
        db_table = 'category'
        managed=False


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, null=False, blank=True, error_messages='The username is required')
    user_rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    description = models.CharField(max_length=150, null=False, blank=True)
    email = models.EmailField(max_length=40, null=False, blank=False, default='*')

    class Meta:
        db_table = 'users'
        managed = False

class AllocationSite(models.Model):
    city = models.CharField(max_length=150, null=False, blank=True)
    address = models.CharField(max_length=150, null=False, blank=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT, null=False, default=None, error_messages={'null':'Please provide an owner for this allocation'})
    ratings=[]
    tags=[]

    class Meta:
        db_table = 'allocation_site'
        managed = False


class CategoryPriority(models.Model):
    """
    Define the priority that an owner wants to give to their location.
    If the user wants to give a high priority to one category over another It will give a 1  max - 10 min
    category score for appears in the filter when users looking for a specific temporal residence category
    """
    allocationSite = models.ForeignKey(AllocationSite, on_delete=models.PROTECT, null=False, default=None)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=False, default=None)
    priority = models.IntegerField(default=0)

    class Meta:
        db_table = 'category_priority'
        managed = False

class MediaData(models.Model):
    """
    Stores allocation aditional data like photos.

    It enhance the creation of user activity feed based on Its preferences and friends activity, showing
    multimedia rellevant data.
    """
    id = models.BigAutoField(primary_key=True)
    allocation = models.ForeignKey(AllocationSite, on_delete=models.PROTECT, null=False, default=None)
    insert_date = models.DateField(null=False, default=None)
    state = models.CharField(null=False, choices=BASE_STATUS, default=BASE_STATUS[0])
    content= models.BinaryField(null=True, default=None)
    url = models.CharField(null=True)

    class Meta:
        db_table = 'media_data'
        managed = False


class Rating(models.Model):
    """
    The rating asigned to an allocation by an user.
    """
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    comment = models.CharField(max_length=150, null=False, blank=True)
    user=models.ForeignKey(User,  on_delete=models.PROTECT, null=False, default=None)
    allocation=models.ForeignKey(AllocationSite, on_delete=models.PROTECT, null=False, default=None)

    class Meta:
        db_table = 'rating'
        managed = False

class Tag(models.Model):
    description = models.CharField(max_length=100)
    state = models.CharField(max_length=1)
    creation_date = models.DateField()

    class Meta:
        db_table = 'tag'
        managed = False

class AllocationSiteTags(models.Model):
    allocation_site_id = models.ForeignKey(AllocationSite, on_delete=models.PROTECT, null=False, default=None, db_column='allocation_site_id')
    tag_id = models.ForeignKey(Tag, on_delete=models.PROTECT, null=False, default=None, db_column='tag_id')
    priority = models.IntegerField()

    class Meta:
        db_table = 'allocation_site_tag'
        managed = False


class AllocationBooking(models.Model):
    PAYMENT_STATUS = [('D', 'Paid'), ('P', 'Pending'), ('T','Partial')]
    allocation_site_id  = models.ForeignKey(AllocationSite, on_delete=models.PROTECT, null=False, default=None)
    start_date = models.DateField()
    end_date = models.DateField()
    number_of_persons = models.IntegerField(validators=[MinValueValidator(0)])
    payment_status = models.CharField(choices=PAYMENT_STATUS)

    class Meta:
        db_table = 'allocation_booking'
        managed = False

class UserInteractions(models.Model):
    #allocation_site =  models.ForeignKey(AllocationSite, on_delete=models.PROTECT, null=False, default=None)
    registry_date = models.DateField()
    activity_entity = models.CharField(db_comment='The table name that the user interacted with')
    activity_id = models.IntegerField(db_comment='The id of the record in the table that the user interacted with')
    user_id = models.ForeignKey(User, on_delete=models.PROTECT, null=False, default=None, db_column='user_id')

    class Meta:
        db_table = 'user_interaction'
        managed = False


class UserContact(models.Model):
    first_user_id = models.ForeignKey(User, on_delete=models.PROTECT, null=False, default=None, related_name='first_user_id', db_column='first_user_id')
    second_user_id = models.ForeignKey(User, on_delete=models.PROTECT, null=False, default=None, related_name='second_user_id', db_column='second_user_id')
    friends_from = models.DateField()
    status = models.CharField(choices=BASE_STATUS)

    class Meta:
        db_table = 'user_contact'
        managed = False

class Country(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    rating = models.IntegerField()
    status = models.CharField(choices=BASE_STATUS)

    class Meta:
        db_table = 'countries'
        managed = False

class State(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    rating = models.IntegerField()
    status = models.CharField(choices=BASE_STATUS)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, null=False, default=None, related_name='country_id',
                      db_column='country_id')

    class Meta:
        db_table = 'states'
        managed = False

class City(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    rating = models.IntegerField()
    status = models.CharField(choices=BASE_STATUS)
    state = models.ForeignKey(State, on_delete=models.PROTECT, null=False, default=None, related_name='state_id',
                      db_column='state_id')

    class Meta:
        db_table = 'cities'
        managed = False