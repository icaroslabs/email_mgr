from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView

from emailer.forms import UnsubscribeForm
from emailer.models import ClientEmail
from emailer.scripts import import_cust


def upload(request):
    if request.method == 'POST':
        import_cust(request.FILES['spreadsheet'])
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


class Unsubscribe(DetailView):
    model = ClientEmail

    def get_context_data(self, **kwargs):
        context = super(Unsubscribe, self).get_context_data(**kwargs)
        context['form'] = UnsubscribeForm
        return context
