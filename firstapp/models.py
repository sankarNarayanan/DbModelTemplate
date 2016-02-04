from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    userName = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.CharField(max_length=100)
