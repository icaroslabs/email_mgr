import sendgrid

from django.utils import timezone

from drss.emailer.models import Campaign
from settings import EMAILER_FROM_ADDR, SENDGRID_USER, SENDGRID_PASSWORD, RINGCENTRAL_POSTFIX


def run():
    e = Emailer()
    e.go(1)


class Emailer():
    def go(self, campaign_id):
        campaign = Campaign.objects.get(pk=campaign_id)
        sg = sendgrid.SendGridClient(SENDGRID_USER, SENDGRID_PASSWORD)
        unsubscribe_link = "<p><a href=%s>Unsubscribe</a></p>"
        email_targets = []
        fax_targets = []
        # emails and faxes indexes match corresponding deltas-1
        emails = [delta.email for delta in campaign.timedelta_set.all()]
        faxes = [delta.fax for delta in campaign.timedelta_set.all()]

        # Calculate new deltas and generate list of targets
        for sub in campaign.subscriber_set.all():
            if sub.last_delta >= (timezone.now() - sub.join_date).days:
                if sub.client.email:
                    email_targets.append(sub)
                elif sub.client.fax:
                    fax_targets.append(sub)
                else: # wut
                    pass
                sub.last_delta += 1
                if sub.last_delta > campaign.timedelta_set.count():
                    sub.delete()
                else:
                    sub.save()

        for target in email_targets:
            message = sendgrid.Mail(
                to=target.client.email,
                subject=emails[target.last_delta-1].subject,
                html=((emails[target.last_delta-1].html) +
                      unsubscribe_link % target.url),
                from_email=EMAILER_FROM_ADDR,
            )
            status, msg = sg.send(message)
            print msg

        #for target in fax_targets:
            #message = sendgrid.Mail(
                #to=target.client.fax + RINGCENTRAL_POSTFIX,
                #subject=faxes[target.last_delta-1].cover,
                #doc=faxes[target.last_delta-1].document,
                #from_email=EMAILER_FROM_ADDR,
            #)
            #status, msg = sg.send(message)
            #print msg

