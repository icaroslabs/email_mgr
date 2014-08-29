from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from emailer.forms import UnsubscribeForm
from emailer.models import ClientEmail
from emailer.scripts import import_cust


def upload(request):
    if request.method == 'POST':
        import_cust(request.FILES['spreadsheet'])
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


class Unsubscribe(DetailView):
    template = 'emailer/unsubscribe.html'

    def get(self, request, pk, **kwargs):
        if pk == '666': # bad strategy
            return ''
        form = UnsubscribeForm()
        return ''

    def post(self, request, pk, **kwargs):
        form = UnsubscribeForm(request['DATA'])
        return ''


class Home(TemplateView):
    template = 'emailer/home.html'


class Success(TemplateView):
    template = 'emailer/success.html'
