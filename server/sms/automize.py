<<<<<<< HEAD
import random
import string

from coupon.models import CouponCode
from customer.models import Customer
from sms.models import SMS, ChainSwitcher
=======
from sms.models import SMS
>>>>>>> Some changes to automising
from sms.serializers import SMSSerializer
from sms.deliver import Router


"""
The time taken for deivering a single message is 2 seconds
which is fucking slow. So, until we set up threading using celery 
Here we should run this script every half hour or so
counting the number of current registered user multiplied by two
and calculate the time taken for delivering all the messages. If the
calculated time exceeds the treshold time of suppose 4 'o' clock, 
we should execute the do statement and start delivering the messages
"""

<<<<<<< HEAD

class SMSEngine(self):

    def __init__(self):
        pass

    def start(self):
=======
class SendSMS(object):

    def __init__(self):
>>>>>>> Some changes to automising
        sms = SMS.objects.all()
        sms_package = SMSSerializer(sms, many=True).data
        for kwargs in sms_package:
            router = Router(**kwargs)
            res = router.send()
<<<<<<< HEAD

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
        
    def post(self):
        customers = Customer.objects.filter(chains__gt=0).distinct()
        for customer in customers:
            try:
                chainswitcher = ChainSwitcher.objects.get(customer=customer)
                chainswitcher.chain_len = len(customer.chains.all())
                chainswitcher.save()
            except ChainSwitcher.DoesNotExist:
                ChainSwitcher(customer=customer, chain_len=len(customer.chains.all())).save()
        self.set_chain(customers)
=======
            # Save log
>>>>>>> Some changes to automising
