from django.views.generic import CreateView, TemplateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from .forms import SignUpForm
from .models import User


class CustomSignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('login')


class CustomLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('conferences_list')


class ConfirmLogoutView(LoginRequiredMixin, TemplateView):
    template_name = 'users/logout.html'


class WelcomeView(TemplateView):
    template_name = 'users/welcome.html'
