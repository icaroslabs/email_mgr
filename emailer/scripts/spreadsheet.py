import sys, re, xlrd

try:
    from emailer.models import Client, Subscriber
except:
    pass

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
    if re.match(EMAIL_PATTERN, s):
        return s
    return None

def qualify_fax(s):
    if re.match(FAX_PATTERN, s):
        return s
    return None

def run(*args):
    if len(args) != 1:
        print (
            "\tUsage: ./manage.py runscript spreadsheet "
            "--script-args=spreadsheet.xls"
        )
        return
    import_customers(args[0])

def import_customers(spreadsheet):
    """
    Parse spreadsheet for email addresses, storing each in a customer record.
    """
    # Excel Spreadsheet .xls
    print spreadsheet
    try:
        book = xlrd.open_workbook(spreadsheet)
        print book.nsheets
    except:
        print "[-] Failed to open " + spreadsheet
        sys.exit(1)

    for sheet in book.sheets():
        print sheet.nrows
        for row in range(sheet.nrows-1):

            try:
                Client.objects.create(
                    email=qualify_email(sheet.cell(row, 1).value)
                )
                print "[+] Successfully created email record"
            except:
                #print "[-] Invalid or existing email %s" % (sheet.cell(row, 1).value)
                pass

            try:
                ClientFax.objects.create(
                    fax=qualify_fax(sheet.cell(row, 0).value)
                )
                print "[+] Successfully created fax record"
            except:
                #print "[-] Invalid or existing fax %s" % (sheet.cell(row, 0).value)
                pass



            #if is_email(str(sheet.cell(row, 1).value)):
                #print "[+] Adding customer record " + sheet.cell(row,1).value
                #cust = Customer.objects.create(email=str(sheet.cell(row,1).value))

            #if is_fax(int(sheet.cell(row, 1).value)):
                #print "[+] Adding broker record " + sheet.cell(row,0).value
                #Broker.objects.create(fax=sheet.cell(row,0).value, Customer=cust)

