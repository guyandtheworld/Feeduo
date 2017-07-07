from django.db import models

from chain.models import Chain
from sms.models import ChainSwitcher


class Customer(models.Model):
    name = models.CharField(max_length=100)
    # Set validator to ensure it's a number
    number = models.CharField(max_length=10, unique=True)
    email = models.EmailField(max_length=70, blank=True, unique=True)
    chains = models.ManyToManyField(Chain, blank=True, related_name="users")

    def save(self, *args, **kwargs):
        if self.pk is not None:
            try:
                switch = ChainSwitcher.objects.get(customer=self)
                switch.chain_len = len(self.chains.all())
                switch.save()
            except ChainSwitcher.DoesNotExist:
                switch = ChainSwitcher(
                    customer=self,
                    chain_len=len(self.chains.all())
                    )
            switch.save()
        super(Customer, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
