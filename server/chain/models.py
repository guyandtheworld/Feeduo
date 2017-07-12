from django.db import models
from django.core.validators import RegexValidator


class Chain(models.Model):
    name = models.CharField(max_length=100)
    chain_code = models.CharField(max_length=6, unique=True)
    email = models.EmailField(max_length=70, unique=True)
    address = models.CharField(max_length=300)
    contact_number = models.CharField(max_length=10)
    number_of_stores = models.IntegerField(default=1)

    class Meta:
        ordering = ('name', )

    def __unicode__(self):
        return self.name