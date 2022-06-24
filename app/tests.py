from msilib.schema import Class
#from django.test import TestCase
from django.db import models


# Create your tests here.

class Train (models.Model):

    title = models.CharField(max_length=250)
    species = models.CharField(max_length=250)

    def __str__(self):
        return self.title

class Test (models.Model):

    title = models.CharField(max_length=250)
    species = models.CharField(max_length=250)

    def __str__(self):
        return self.title