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

    def set_chain(self, customers, **kwargs):
        SMS.objects.all().delete()
        for customer in customers:
            # customer.chains.all().order_by('names')
            num = customer.number
            if num.isdigit() and len(num)==10:
                if len(customer.chains.all())==1:
                    chain = customer.chains.first()
                else:
                    switch = ChainSwitcher.objects.get(customer=customer)
                    chain = customer.chains.all()[switch.switcher-1]
                    if switch.switcher == switch.chain_len:
                        switch.switcher = 1
                    else:
                        switch.switcher+=1
                    switch.save()
                coupon = random.choice(chain.coupons.all()).message
                SMS(number=int(num), message_body=coupon).save()

    def process_sms(self, **kwargs):
        texts = []
        for sms in SMS.objects.all():
            texts.append([sms.number, sms.message_body])
            
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
        self.set_chain(customers)
        self.process_sms()
        return Response({"STATUS": "OK"}, status.HTTP_202_ACCEPTED)
