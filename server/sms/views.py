from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from customer.models import Customer
from sms.models import SMS, ChainSwitcher
#Temperory
from customer.serializers import CustomerChainSerializer

class SendSMS(APIView):

    permission_classes = (IsAuthenticated,)

    # def set_chain(self, customers, **kwargs):
    #     for customer in customers:
    #         customer.chains.all().order_by('names')

    # def process_sms(self, customers, **kwargs):
    #     pass

    def get(self, response, format=None):
        return Response({'status': 'Okay, I guess?'}, status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS)

    def post(self, response, format=None):
        customers = Customer.objects.filter(chains__gt=1).distinct()
        """
        TODO
        load all customer data with more that one chain
        cross check with customer if new user added
        if yes, add onto ChainSwitcher. From ChainSwitcher get data
        of customer of which chain to send sms and increment the data
        If more than two chains are present else just let it be also 
        also cross check with the length of chains related to the customer
        to keep the length updated.

        """
        serializer = CustomerChainSerializer(customers, many=True)
        return Response(serializer.data, status.HTTP_202_ACCEPTED)