from django.contrib.auth.models import User
from django.db import models


class Chain(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=70, blank=True)
    address = models.CharField(max_length=300)
    contact_number = models.CharField(max_length=10)
    number_of_stores = models.IntegerField(default=1)

    def __unicode__(self):
        return self.name