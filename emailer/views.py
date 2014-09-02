from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from emailer.forms import UnsubscribeForm
from emailer.models import ClientEmail
from emailer.scripts import check_email, import_cust, unsubscribe


def upload(request):
    if request.method == 'POST':
        import_cust(request.FILES['spreadsheet'])
    else:
        return redirect(request.META['HTTP_REFERER'])


class Home(TemplateView):
    template_name = 'emailer/home.html'


class Unsubscribe(DetailView):
    model = ClientEmail

    def get(self, request, pk):
        form = UnsubscribeForm()
        return render(request, 'emailer/unsubscribe.html', {'form': form})

    # upon form validation, include cust_id querystring and user submitted
    # email in context object
    def post(self, request, pk):
        form = UnsubscribeForm(data=request.POST)
        if form.is_valid():
            if check_email.check_email(form.cleaned_data['email'], pk):
                # unsubscribe
                return render(request, 'emailer/success.html')
        else:
            return render(request, 'emailer/unsubscribe.html', {'form': form})


class Success(TemplateView):
    template_name = 'emailer/success.html'
