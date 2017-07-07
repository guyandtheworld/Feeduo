from django.core.validators import MaxValueValidator
from django.db import models


class SMS(models.Model):
    number = models.PositiveIntegerField(unique=True, validators=[MaxValueValidator(9999999999)])
    message_body = models.CharField(max_length=140)

    def __unicode__(self):
        return "{}".format(self.number)


class ChainSwitcher(models.Model):
    customer = models.OneToOneField('customer.Customer', related_name="switcher", on_delete=models.CASCADE)
    switcher = models.PositiveIntegerField(validators=[MaxValueValidator(100)], default=1)
    chain_len = models.PositiveIntegerField(validators=[MaxValueValidator(100)])

    def __unicode__(self):
        return "{}".format(self.customer.name)
