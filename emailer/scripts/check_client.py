import emailer.models as emailer_models

def run(*args):
    if len(args) != 2:
        print (
            "\tUsage: ./manage.py runscript check_email "
            "--script-args=email cust_id"
        )
        return
    CheckClient(email=args[0], cust_id=args[1])

class CheckClient():
    """
    Return true if given email matches cust_id
    """
    def __init__(self, **kwargs):
        return emailer_models.ClientEmail.objects.get(email=kwargs['email']).cust_id == kwargs['cust_id']



