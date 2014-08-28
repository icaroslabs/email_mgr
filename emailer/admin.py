from django.contrib import admin
from .models import *


class SpreadsheetAdmin(admin.ModelAdmin):
    pass


class EmailTemplateAdmin(admin.ModelAdmin):
    pass


class ClientFaxAdmin(admin.ModelAdmin):
    pass


class ClientEmailAdmin(admin.ModelAdmin):
    pass


class EmailSubscriberAdmin(admin.ModelAdmin):
    pass


class EmailNonsubscriberAdmin(admin.ModelAdmin):
    pass


class FaxSubscriberAdmin(admin.ModelAdmin):
    pass


class FaxNonsubscriberAdmin(admin.ModelAdmin):
    pass



admin.site.register(Spreadsheet, SpreadsheetAdmin)
admin.site.register(EmailTemplate, EmailTemplateAdmin)
admin.site.register(ClientFax, ClientFaxAdmin)
admin.site.register(ClientEmail, ClientEmailAdmin)
admin.site.register(EmailSubscriber, EmailSubscriberAdmin)
admin.site.register(EmailNonsubscriber, EmailNonsubscriberAdmin)
admin.site.register(FaxSubscriber, FaxSubscriberAdmin)
admin.site.register(FaxNonsubscriber, FaxNonsubscriberAdmin)
