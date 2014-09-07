from django.core.mail import send_mail
from django.utils import timezone

from settings import EMAILER_FROM_ADDR

try:
    from ..models import Subscriber
except:
    pass

def run():
    e = Emailer()
    e.go()


class Emailer():
    def go(self):
        recipients = []
        for target in Subscriber.objects.all():
            delta = (timezone.now() - target.join_date)
            if (delta.days >= target.campaign.fifth_time_delta):
                target.last_delta = 5
                target.save()
                recipients += target
            elif (delta.days >= target.campaign.fourth_time_delta):
                target.last_delta = 4
                recipients += target.save()
            elif (delta.days >= target.campaign.third_time_delta):
                target.last_delta = 3
                recipients += target.save()
            elif (delta.days >= target.campaign.second_time_delta):
                target.last_delta = 2
                recipients += target.save()
            elif (delta.days >= target.campaign.first_time_delta):
                target.last_delta = 1
                target.save()
                recipients += target
            else: # or else wut nigga
                pass # dats right nigga

        for recipient in recipients:
            subject = recipient.campaign.first_email.subject
            body = recipient.campaign.first_email.body + recipient.url
            sender = EMAILER_FROM_ADDR
            send_mail(subject, body, sender, recipient)
