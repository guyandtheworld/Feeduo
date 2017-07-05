from rest_framework import serializers

from models import Coupon


class CouponSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Coupon
        fields = ("chain", "coupon_name", "message", "unique_code", "expiry_date")