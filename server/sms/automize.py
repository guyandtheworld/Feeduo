from django_cron import CronJobBase, Schedule

from sms.models import SMS
from sms.serializers import SMSSerializer
from sms.process import Router

class SendSMS(CronJobBase):
    RUN_AT_TIMES = ['15:52']
    MIN_NUM_FAILURES = 1

    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'sms.automize.SendSMS'

    def do(self):
        sms = SMS.objects.all()
        sms_package = SMSSerializer(sms, many=True)

        for kwargs in sms_package:
            router = Router(**kwargs)
            router.setUp()
            router.send()

