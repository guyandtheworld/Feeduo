from sms.models import SMS
from sms.serializers import SMSSerializer
from sms.process import Router

"""
The time taken for deivering a single message is 2 seconds
which is fucking slow. So, until we set up threading using celery 
Here we should run this script every half hour or so
counting the number of current registered user multiplied by two
and calculate the time taken for delivering all the messages. If the
calculated time exceeds the treshold time of suppose 4 'o' clock, 
we should execute the do statement and start delivering the messages
"""

class SendSMS(object):

    def __init__(self):
        sms = SMS.objects.all()
        sms_package = SMSSerializer(sms, many=True).data
        for kwargs in sms_package:
            router = Router(**kwargs)
            res = router.send()
            # Save log
