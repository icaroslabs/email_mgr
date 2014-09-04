from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from django import forms

class SpreadsheetForm(forms.Form):
    pass


class UnsubscribeForm(forms.Form):
    email = forms.EmailField(
        label = "Enter your email address",
        required = True,
        max_length = 100, 
    )
#     cust_id = forms.CharField(
#         required=False,
#         widget=forms.HiddenInput(),
#     )

    def __init__(self, *args, **kwargs):
        super(UnsubscribeForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.form_id = 'id-unsubscribeForm'
        self.form_class = 'bootstrap'
        self.form_method = 'post'
        self.form_action = 'submit-unsubscribe'
        self.helper.add_input(Submit('submit', 'Submit'))
