from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Conference, Presentation
from .forms import RegisterPresentationForm


class ConferencesListView(LoginRequiredMixin, ListView):
    model = Conference
    template_name = 'conferences/conferences_list.html'
    context_object_name = 'conferences'
    paginate_by = 10


class ConferenceDetailView(DetailView):
    model = Conference
    template_name = 'conferences/conference_detail.html'
    context_object_name = 'conference'


class RegisterPresentationView(LoginRequiredMixin, CreateView):
    model = Presentation
    form_class = RegisterPresentationForm
    template_name = 'conferences/register_presentation.html'
