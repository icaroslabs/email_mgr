import sendgrid

from django.utils import timezone

from drss.emailer.models import Campaign
from settings import EMAILER_FROM_ADDR, SENDGRID_USER, SENDGRID_PASSWORD


def run():
    e = Emailer()
    e.go()


class Emailer():
    def calculate_delta(self, sub, targets):
        if sub.last_delta >= (timezone.now() - sub.join_date).days:
            sub.last_delta += 1
            sub.save()
            targets.append(sub)

    def go(self, campaign):
        sg = sendgrid.SendGridClient(SENDGRID_USER, SENDGRID_PASSWORD)
        link = "<p><a href=%s>Unsubscribe</a></p>"
        targets = []
        emails = [delta.email for delta in campaign.timedelta_set.all()]

        for sub in campaign.subscriber_set.all():
            self.calculate_delta(sub)


        for target in targets:

            message = sendgrid.Mail(
                to=target.email,
                subject=campaign.timedelta_set.get(),
                html=,
                text=,
                from_email=EMAILER_FROM_ADDR
            )
            status, msg = sg.send(message)
            print msg

