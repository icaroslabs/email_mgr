from django.contrib import admin
from .models import *


class ClientAdmin(admin.ModelAdmin):
    read_only = ('slug',)


class TimeDeltaAdmin(admin.ModelAdmin):
    pass

class EmailTemplateAdmin(admin.ModelAdmin):
    pass


class CampaignAdmin(admin.ModelAdmin):
    pass


class SubscriberAdmin(admin.ModelAdmin):
    read_only = ('client', 'campaign', 'join_date',)


class SpreadsheetAdmin(admin.ModelAdmin):
    pass



admin.site.register(Client, ClientAdmin)
admin.site.register(TimeDelta, TimeDeltaAdmin)
admin.site.register(EmailTemplate, EmailTemplateAdmin)
admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Spreadsheet, SpreadsheetAdmin)
