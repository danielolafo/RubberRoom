from django.db import models

class User(models.Model):
    def __init__(self):
        username = models.CharFiel(max_length=30)
        email = models.EmailField
        rating = models.DecimalField(max_length=3,decimal_places=1)
        description = models.CharField(max_length=150)