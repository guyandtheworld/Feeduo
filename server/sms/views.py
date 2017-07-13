import random
import string

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from coupon.models import CouponCode
from customer.models import Customer
from sms.models import SMS, ChainSwitcher


class SendSMS(APIView):

    permission_classes = (IsAuthenticated,)

    def hash_function(self): 
        code_str = ''.join(random.choice(string.ascii_uppercase) for _ in range(4))
        code_dig = str(random.randint(10, 99))
        code = code_str + code_dig
        return code

    def set_chain(self, customers, **kwargs):
        SMS.objects.all().delete()
        for customer in customers:
            # customer.chains.all().order_by('names')
            num = customer.number
            customer_chain = customer.chains.all()
            if num.isdigit() and len(num)==10:
                if len(customer_chain)==1:
                    chain = customer_chain[0]
                else:
                    switch = ChainSwitcher.objects.get(customer=customer)
                    chain = customer_chain[switch.switcher-1]
                    if switch.switcher == switch.chain_len:
                        switch.switcher = 1
                    else:
                        switch.switcher+=1
                    switch.save()
                code = self.hash_function()
                coupon = random.choice(chain.coupons.all()).message
                body = "{}- Use {} code to redeem offer.".format(coupon, code)
                sms = SMS(
                        number=int(num),
                        message=body,

                    )
                sms.save()
                CouponCode(
                        sms=sms,
                        code=code
                    ).save()
        

    def process_sms(self, **kwargs):
        texts = []
        for sms in SMS.objects.all():
            texts.append([sms.number, sms.message_body])
        print(texts)

    def get(self, response, format=None):
        return Response({'status': 'Okay, I guess?'}, status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS)

    def post(self, response, format=None):

        customers = Customer.objects.filter(chains__gt=0).distinct()

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
