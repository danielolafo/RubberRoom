from django.db import models

class Category(models.Model):

    def __init__(self):
        self.name = models.CharField(max_length=150)