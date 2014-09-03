from emailer.models import ClientEmail

def run(*args):
    if len(args) != 2:
        print (
            "\tUsage: ./manage.py runscript check_email "
            "--script-args=email cust_id"
        )
        return
    check_email(email=args[0], cust_id=args[1])

def check_email(email, cust_id):
    """
    Return true if given email matches cust_id
    """
    try:
        print (ClientEmail.objects.get(pk=cust_id).email == email)
        return (ClientEmail.objects.get(pk=cust_id).email == email)
    except:
        print False
        return False
