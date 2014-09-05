from django.core.email import send_mail
from django.utils import timezone

from settings import EMAILER_FROM_ADDR

try:
    from emailer.models import Subscriber
except:
    pass

def run():
    pass

def emailer():
    for target in Subscribers.objects.all():
        delta = (timezone.now() - target.join_date)
        if (delta.days >= target.campaign.fifth_time_delta):
            target.last_delta = 5
            recipients += target.save()
        else if (delta.days >= target.campaign.fourth_time_delta):
            target.last_delta = 4
            recipients += target.save()
        else if (delta.days >= target.campaign.third_time_delta):
            target.last_delta = 3
            recipients += target.save()
        else if (delta.days >= target.campaign.second_time_delta):
            target.last_delta = 2
            recipients += target.save()
        else if (delta.days >= target.campaign.first_time_delta):
            target.last_delta = 1
            recipients += target.save()
        else: # or else wut nigga
            pass # dats right nigga

    for recip in recipients:
        # get to_addr and body from Subscriber object fk relation chain
        # send_mail()
