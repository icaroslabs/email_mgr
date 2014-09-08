from __future__ import unicode_literals

from mezzanine import template

from emailer.forms import SpreadsheetForm

register = template.Library()

@register.inclusion_tag("admin/includes/quick_spreadsheet.html", takes_context=True)
def quick_spreadsheet(context):
    form = SpreadsheetForm()
    context['form'] = form
    return context
