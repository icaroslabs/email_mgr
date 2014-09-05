drss
====
The emailer script needs to be finished. The slug field on the subsciber.client chain
can be used to create a unique ubsubscribe url. Just drop it in the email body before
sending it out. Also, the script needs to be able to choose an email template based
on the current time delta.

In order to make the subscriber and nonsubscriber tables unique, I overrode their
save methods to make the required checks.

The spreadsheet script is used to mass import emails and faxes from an xls file. It
currently only supports xls (not csv, not xlsx). It will parse any xls tho and will
validate emails and fax numbers on the fly. It only requires that faxes be in the 
first column (index 0) and email address be in the second column (index 1).

Unsubscribe form functionality works fine, altho it needs a page to sit on.
