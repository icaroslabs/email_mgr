import csv, sys, re, xlrd

from drss.emailer import models as emailer_models


FAX_PATTERN = re.compile((
    "\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d"
    "{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}"
))

EMAIL_PATTERN = re.compile((
    "([a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`"
    "{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|"
    "\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"
))

def qualify_email(s):
    return re.match(EMAIL_PATTERN, s)

def qualify_fax(s):
    return re.match(FAX_PATTERN, s)

def run(*args):
    if len(args) != 2:
        print (
            "Usage: ./manage.py runscript spreadsheet "
            "--script-args=<filename>, <campaign_id>"
        )
        return 1
    import_clients(args[0], args[1])

def import_clients(spreadsheet, campaign_id):
    """
    Parse spreadsheet for emails and faxes, storing each in a
    unique client record.
    """
    try:
        campapign = emailer_models.Campaign.objects.get(pk=campaign_id)
    except:
        print "Campaign does not exist. Try one of these."
        print ", ".join([str(cam.pk) for cam in emailer_models.Campaign.objects.all()])
        return 1
    try:
        reader = csv.reader(open(spreadsheet))
        print '[+] Initialized reader object'
    except Exception, e:
        print '[-] %s' % e
        return 1

    for row in reader:
        if qualify_fax(str(row[0])):
            emailer_models.Client.objects.create(
                fax=str(row[0]),
                campaign=campaign,
            )

        if qualify_email(str(row[1])):
            emailer_models.Client.objects.create(
                email=str(row[1]),
                campaign=campaign,
            )
    return 0

