from django.contrib import admin
from .models import *


class ClientAdmin(admin.ModelAdmin):
    fields = ('email', 'fax',)


class EmailTemplateAdmin(admin.ModelAdmin):
    pass


class CampaignAdmin(admin.ModelAdmin):
    pass


class SubscriberAdmin(admin.ModelAdmin):
    pass


class NonsubscriberAdmin(admin.ModelAdmin):
    pass


class SpreadsheetAdmin(admin.ModelAdmin):
    pass



admin.site.register(Client, ClientAdmin)
admin.site.register(EmailTemplate, EmailTemplateAdmin)
admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Nonsubscriber, NonsubscriberAdmin)
admin.site.register(Spreadsheet, SpreadsheetAdmin)
