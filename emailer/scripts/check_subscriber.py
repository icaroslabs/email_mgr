from emailer.models import Subscriber

def run(*args):
    if len(args) != 2:
        print (
            "\tUsage: ./manage.py runscript check_subscriber"
            "--script-args=email"
        )
        return
    check_subscriber(email=args[0])

def check_subscriber(email):
    """
    Return true if given email matches a subscriber
    """
    try:
        return (Subscriber.objects.get())
    except:
        print False
        return False
