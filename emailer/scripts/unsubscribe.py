from emailer.models import ClientEmail, EmailSubscriber, EmailNonsubscriber
from email.scripts import check_subscriber

def run(*args):
    if len(args) != 1:
        print (
            "\tUsage: ./manage.py runscript unsubscribe "
            "--script-args=email"
        )
        return
    unsubscribe(args[0])

def unsubscribe(email):
    """
    Check if email matches a current Subscriber. Removes Subscriber
    and creates Nonsubscriber, or does nothing.
    """
    if check_subscriber.check_subscriber(email):
        pass
    else:
        print "Email does not match a subscriber"
        return

