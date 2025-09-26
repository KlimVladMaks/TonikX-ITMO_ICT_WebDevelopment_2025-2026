from django.views.generic import CreateView
from django.views import View
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import SignUpForm
from .models import User


class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('login')


# Временное представление-заглушка
class LoginView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("login", content_type="text/plain")
