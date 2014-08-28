from django import forms

from emailer.models import Spreadsheet

class SpreadsheetForm(forms.ModelForm):
    class Meta:
        model = Spreadsheet
        fields = ['spreadsheet',]


class UnsubscribeForm(forms.Form):
    pass
