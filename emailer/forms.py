from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from django import forms

from emailer.models import Spreadsheet
from emailer.scripts.spreadsheet import import_customers


class SpreadsheetForm(forms.ModelForm):
    model = Spreadsheet

    def save(self):
        import_customers(self)

    def __init__(self, *args, **kwargs):
        super(SpreadsheetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_id = 'id-spreadsheetForm'
        self.form_class = 'bootstrap'
        self.form_method = 'post'
        self.form_action = ''
        self.helper.add_input(Submit('submit', 'Submit'))


class UnsubscribeForm(forms.Form):
    email = forms.EmailField(
        label = "Enter your email address",
        required = True,
        max_length = 100, 
    )

    def __init__(self, *args, **kwargs):
        super(UnsubscribeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_id = 'id-unsubscribeForm'
        self.form_class = 'bootstrap'
        self.form_method = 'post'
        self.form_action = 'submit-unsubscribe'
        self.helper.add_input(Submit('submit', 'Submit'))
