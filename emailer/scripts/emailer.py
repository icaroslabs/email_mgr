import sendgrid

from django.utils import timezone

from drss.emailer.models import Campaign
from settings import EMAILER_FROM_ADDR, SENDGRID_USER, SENDGRID_PASSWORD


def run():
    e = Emailer()
    e.go()


class Emailer():
    def calculate_deltas(self):
        deltas = [
            [], # Unused
            [], # Delta 1
            [], # Delta 2
            [], # Delta 3
            [], # Delta 4
            [], # Delta 5
        ]

        for sub in cam.subscriber_set.all():
            if sub.last_delta < 5:
                deltas[sub.last_delta].append( (str(sub), sub.url) )
            else:
                deltas[5].append(str(sub))

        return deltas

    def go(self):
        sg = sendgrid.SendGridClient(SENDGRID_USER, SENDGRID_PASSWORD)
        link = "<p><a href=%s>Unsubscribe</a></p>"


        for cam in Campaign.objects.all():
            first_email = cam.first_email
            second_email = cam.second_email
            third_email = cam.third_email
            fourth_email = cam.fourth_email
            fifth_email = cam.fifth_email

            # Calculate deltas
            deltas = self.calculate_deltas()

            # First delta
            for delta in deltas[0]:
                message = sendgrid.Mail(
                    to=[delta[0]],
                    subject=first_email.subject,
                    html=first_email.html + (link % delta[1]),
                    text=first_email.text,
                    from_email=EMAILER_FROM_ADDR
                )
                status, msg = sg.send(message)
                print msg

