from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from emailer.forms import UnsubscribeForm
from emailer.models import ClientEmail
from emailer.scripts import import_cust


def upload(request):
    if request.method == 'POST':
        import_cust(request.FILES['spreadsheet'])
    return redirect(request.META['HTTP_REFERER'])
class Home(TemplateView):
    template_name = 'emailer/home.html'


class Unsubscribe(DetailView):
    model = ClientEmail

    def get(self, request, **kwargs):
        form = UnsubscribeForm()
        return render(request, 'emailer/unsubscribe.html', {'form': form})

    # upon form validation, include cust_id querystring and user submitted 
    # email in context object
    def post(self, request, **kwargs):
        form = UnsubscribeForm(data=request.POST)
        context = {'form': form}
    	return render(request, 'emailer/unsubscribe.html', context)


class SubmitUnsubscribe(TemplateView):
    template_name = 'emailer/submit-unsubscribe.html'

    # get method should be unreachable, but return to sender
    def get(self, request, **kwargs):
        return redirect(request.META['HTTP_REFERER'])

    # check that cust_id corresponds with provided email
    def post(self, request, **kwargs):
        return redirect(request.META['HTTP_REFERER'])
    


class SuccessUnsubscribe(TemplateView):
    template_name = 'emailer/success.html'
