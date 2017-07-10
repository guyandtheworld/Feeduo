from rest_framework import serializers

from models import Coupon, CouponCode

from sms.serializers import SMSSerializer


class CouponSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Coupon
        fields = ("chain", "coupon_name", "message", "unique_code", "expiry_date")


class VerifyCouponSerializer(serializers.ModelSerializer):
    # sms = SMSSerializer(read_only=True)
    class Meta:
        model = CouponCode
        fields = ("sms", "code")