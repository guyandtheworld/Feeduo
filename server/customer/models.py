from django.db import models

from chain.models import Chain
from sms.models import ChainSwitcher


class Customer(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=10, unique=True)
    email = models.EmailField(max_length=70, unique=True)
    chains = models.ManyToManyField(Chain, blank=True, related_name="users")

    def __unicode__(self):
        return self.name
