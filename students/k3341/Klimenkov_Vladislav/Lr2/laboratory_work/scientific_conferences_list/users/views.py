from django.views.generic import CreateView
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from .models import User


class CustomSignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('login')


class CustomLoginView(View):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    # success_url = reverse_lazy('main_menu')
