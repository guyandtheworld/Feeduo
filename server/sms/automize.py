import random
import string
import threading

from coupon.models import CouponCode
from customer.models import Customer
from sms.models import SMS, ChainSwitcher
from sms.serializers import SMSSerializer
from sms.deliver import Router


class MakeDatabase(object):
    """
        Prepares database of fresh SMS
    """
    def __init__(self):
        self.make_database()

    def hash_function(self): 
        code_str = ''.join(random.choice(string.ascii_uppercase) for _ in range(4))
        code_dig = str(random.randint(10, 99))
        code = code_str + code_dig
        return code

    def set_chain(self, customers, **kwargs):
        SMS.objects.all().delete()
        for customer in customers:
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
                sender_id = chain.chain_code
                code = self.hash_function()
                coupon = random.choice(chain.coupons.all()).message
                body = "{}- Use {} code to redeem offer.".format(coupon, code)
                sms = SMS(
                        number=int(num),
                        message=body,
                        sender_id=sender_id,
                    )
                sms.save()
                CouponCode(
                        sms=sms,
                        code=code
                    ).save()
        
    def make_database(self):
        customers = Customer.objects.filter(chains__gt=0).distinct()
        for customer in customers:
            try:
                chainswitcher = ChainSwitcher.objects.get(customer=customer)
                chainswitcher.chain_len = len(customer.chains.all())
                chainswitcher.save()
            except ChainSwitcher.DoesNotExist:
                ChainSwitcher(customer=customer, chain_len=len(customer.chains.all())).save()
        self.set_chain(customers)


class DeliverSMS(threading.Thread):
    def __init__(self, **kwargs):
        threading.Thread.__init__(self)
        self.kwargs = kwargs

    def go(self, **kwargs):
        r = Router(**kwargs)
        r.send()

    def run(self):
        self.go(**self.kwargs)


class SMSEngine(object):

    def __init__(self):
        MakeDatabase()

    def start_delivery(self):
        """
            Gets all prepared SMS and splits it into groups of 500
            and sends the sms 500 at a time by using threading.
        """
        sms = SMS.objects.all()
        sms_package = SMSSerializer(sms, many=True).data
        number_of_sms = len(sms_package)
        sms_count = 0
        for i in range(1, number_of_sms, 500):
            sms_threads = []
            while len(sms_package[sms_count:i+500])>0:
                sms_threads.append(DeliverSMS(**sms_package[sms_count]))
                sms_count+=1
            for sms in sms_threads:
                sms.start()
            for sms in sms_threads:
                sms.join()
