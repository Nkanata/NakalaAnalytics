from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from .forms import SignUpForm


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
