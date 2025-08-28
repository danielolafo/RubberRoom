from django.db import models

class Rating(models.Model):

    def __init__(self):
        self.rating= models.DecimalField(max_digits=3, decimal_places=1)
        self.comment = models.CharField(max_length=150)