from django.db import models

from chain.models import Chain


class Coupon(models.Model):
    chain = models.ForeignKey(Chain, related_name="coupons", on_delete=models.CASCADE)
    coupon_name = models.CharField(max_length=7, unique=True)
    message = models.CharField(max_length=120)
    unique_code = models.CharField(max_length=8)
    publish_date = models.DateField(auto_now_add=True)
    expiry_date = models.DateField()

    def __unicode__(self):
        return self.coupon_name

    class Meta:
        ordering = ('expiry_date', )