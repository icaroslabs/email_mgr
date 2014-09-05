try:
    from emailer.models import Subscriber
except:
    pass


def run():
    pass

def emailer():
    targets = Subscribers.objects.all()

    for target in targets:
       pass 
