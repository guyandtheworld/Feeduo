from django.http import Http404

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from coupon.models import Coupon
from coupon.serializers import CouponSerializer



class CouponList(APIView):
    """
    Create Coupon or view all Coupons
    """

    def get(self, request, format=None):
        Coupons = Coupon.objects.all()
        serializer = CouponSerializer(Coupons, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
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

    def get_object(self, pk):
        try:
            return Coupon.objects.get(pk=pk)
        except Coupon.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Coupon = self.get_object(pk)
        serializer = CouponSerializer(Coupon)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        Coupon = self.get_object(pk)
        serializer = CouponSerializer(Coupon, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Coupon = self.get_object(pk)
        Coupon.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
