import random

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

    def set_chain(self, switchers, **kwargs):
        for switch in switchers:
            # customer.chains.all().order_by('names')
            num = switch.customer.number
            if num.isdigit() and len(num)==10 and len(switch.customer.chains.all())>0:
                if len(switch.customer.chains.all())==1:
                    message_body = random.choice(c.customer.chains.first().coupons.all()).message
                else:
                    print(switch.customer.chains.all())
                    print(switch.switcher)
                    message_body = switch.customer.chains.all()[switch.switcher]
                    if switch.switcher == switch.chain_len:
                        switch.switcher = 1
                    else:
                        switch.switcher+=1
                    switch.save()
                SMS(number=int(num), message_body=message_body).save()

    def process_sms(self, **kwargs):
        pass
        """
            Send trigger to celery to send the sms from the database
        """

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
        for customer in customers:
            try:
                chainswitcher = ChainSwitcher.objects.get(customer=customer)
                chainswitcher.chain_len = len(customer.chains.all())
                chainswitcher.save()
            except ChainSwitcher.DoesNotExist:
                ChainSwitcher(customer=customer, chain_len=len(customer.chains.all())).save()
        self.set_chain(ChainSwitcher.objects.all())
        return Response(serializer.data, status.HTTP_202_ACCEPTED)
