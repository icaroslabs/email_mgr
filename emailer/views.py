from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from emailer.forms import UnsubscribeForm
from emailer.models import ClientEmail


def upload(request):
    if request.method == 'POST':
        pass
    else:
        return redirect(request.META['HTTP_REFERER'])


class Home(TemplateView):
    template_name = 'emailer/home.html'


class Unsubscribe(DetailView):
    model = Client

    def _validate_email(self, email, cust_id):
        try:
            cust = Client.objects.get(email=email).slug
        except:
            return False
        else:
            return cust == slug

    def _unsubscribe(self, email):
        if True: # email matches subscriber
            pass # create nonsub and delete sub

    def get(self, request, pk):
        form = UnsubscribeForm()
        return render(request, 'emailer/unsubscribe.html', {'form': form})

    def post(self, request, pk):
        form = UnsubscribeForm(data=request.POST)
        if form.is_valid():
            if self._validate_email(form.cleaned_data['email'], pk):
                self.unsubscribe(form.cleaned_data['email'])
                return render(request, 'emailer/success.html')
            else:
                return render(request, 'emailer/fail.html')
        else:
            return render(request, 'emailer/unsubscribe.html', {'form': form})


class Success(TemplateView):
    template_name = 'emailer/success.html'
