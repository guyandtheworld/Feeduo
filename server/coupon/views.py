import json

from django.http import Http404
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from chain.models import Chain
from sms.models import SMS

from models import Coupon, CouponCode
from permissions import IsPostOrIsAuthenticated
from serializers import CouponSerializer, VerifyCouponSerializer


class CouponList(APIView):
    """
    Create Coupon or view all Coupons
    """
    permission_classes = (IsAuthenticated,)


    def get(self, request, pk, format=None):
        chain = Chain.objects.get(pk=pk)
        Coupons = chain.coupons.all()
        serializer = CouponSerializer(Coupons, many=True)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        # Add functionality for saving without explicitely providing chain in the data
        serializer = CouponSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CouponDetail(APIView):
    """
    Retrieve, update, delete a Coupon
    """
    
    permission_classes = (IsAuthenticated,)

    def get_chain(self, pk):
        try:
            return Chain.objects.get(pk=pk)
        except Chain.DoesNotExist:
            raise Http404

    def get_coupon(self, chain, pk):
        try:
            return Coupon.objects.get(chain=chain, pk=pk)
        except Coupon.DoesNotExist:
            raise Http404

    def get(self, request, format=None, **kwargs):
        pk_chain = self.kwargs.get('pk_chain')
        pk_coupon = self.kwargs.get('pk_coupon')
        chain = self.get_chain(pk_chain)
        coupon = self.get_coupon(chain, pk_coupon)
        serializer = CouponSerializer(coupon)
        return Response(serializer.data)

    def post(self, request, format=None, **kwargs):
        pk_chain = self.kwargs.get('pk_chain')
        pk_coupon = self.kwargs.get('pk_coupon') 
        chain = self.get_chain(pk_chain)
        coupon = self.get_coupon(chain, pk_coupon)
        serializer = CouponSerializer(coupon, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None, **kwargs):
        pk_chain = self.kwargs.get('pk_chain')
        pk_coupon = self.kwargs.get('pk_coupon') 
        chain = self.get_chain(pk_chain)
        coupon = self.get_coupon(chain, pk_coupon)
        coupon.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VerifyCoupon(APIView):

    def get(self, request, format=None, **kwargs):
        number = request.POST.get('number')
        print(number)
        code = request.POST.get('code')
        sms = get_object_or_404(SMS, number=number)
        print(code)
        coupon_code = CouponCode.objects.get(sms=sms).code
        if coupon_code == code:
            message = sms.message_body.split('-')[0]
            data = {}
            data["message"] = message
            return Response(data)
        else:
            return Response("{'message': 'Wrong code'}")

    def post(self, request, format=None, **kwargs):
        number = request.POST.get('number')
        code = request.POST.get('code')
        sms = get_object_or_404(SMS, number=number)
        sms.delete()
        json = {}
        json["Result"] = "Thanks for coming! Do visit again!"
        return Response(json)
