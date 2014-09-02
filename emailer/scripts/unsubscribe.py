from emailer.models import ClientEmail, EmailSubscriber, EmailNonsubscriber

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
    Remove a client from subscribers and place in nonsubscribers
    """
    try:
        client = ClientEmail.objects.get(email=email)
    except:
        print "Client email not found. %s" % email
    try:
        EmailNonsubscriber.objects.create(nonsubscriber=client)
    except:
        print "Error creating nonsubscriber \t %s" % client.email
    try:
        EmailSubscriber.objects.delete(subscriber=client)
    except:
        print "Error deleting subscriber \t %s" % client.email

