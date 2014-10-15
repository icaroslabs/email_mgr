from django.contrib import admin
from .models import *


class ClientAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)


class TimeDeltaInline(admin.TabularInline):
    model = TimeDelta
    extra = 4


class EmailTemplateAdmin(admin.ModelAdmin):
    pass


class FaxTemplateAdmin(admin.ModelAdmin):
    pass


class SpreadsheetAdmin(admin.ModelAdmin):
    pass


class SpreadsheetInline(admin.TabularInline):
    model = Spreadsheet
    extra = 1


class CampaignAdmin(admin.ModelAdmin):
    inlines = [TimeDeltaInline, SpreadsheetInline]


class SubscriberAdmin(admin.ModelAdmin):
    readonly_fields = (
        'client', 'join_date', 'campaign',
        'url', 'last_delta', 'last_activity',
    )


admin.site.register(Client, ClientAdmin)
admin.site.register(EmailTemplate, EmailTemplateAdmin)
admin.site.register(FaxTemplate, FaxTemplateAdmin)
admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
