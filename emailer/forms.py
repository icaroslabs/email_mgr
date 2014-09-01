from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from django import forms

from emailer.models import Spreadsheet

class SpreadsheetForm(forms.ModelForm):
    class Meta:
        model = Spreadsheet
        fields = ['spreadsheet',]


class UnsubscribeForm(forms.Form):
    submit_email = forms.EmailField(
        label = "Enter your email address",
        required = True,
        max_length = 100, 
    )

    def __init__(self, *args, **kwargs):
        super(UnsubscribeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_id = 'id-unsubscribeForm'
        self.form_class = 'x-porn'
        self.form_method = 'post'
        self.form_action = 'submit-unsubscribe'
        self.helper.add_input(Submit('submit', 'Submit'))
