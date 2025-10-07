from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .models import Conference, Presentation, Review
from .forms import RegisterPresentationForm


class ConferencesListView(LoginRequiredMixin, ListView):
    model = Conference
    template_name = 'conferences/conferences_list.html'
    context_object_name = 'conferences'
    paginate_by = 10


class ConferenceDetailView(LoginRequiredMixin, DetailView):
    model = Conference
    template_name = 'conferences/conference_detail.html'
    context_object_name = 'conference'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        conference = self.object
        user_presentations = Presentation.objects.filter(
            conference=conference, 
            author=self.request.user
        )
        context['user_presentations'] = user_presentations
        return context


class RegisterPresentationView(LoginRequiredMixin, CreateView):
    model = Presentation
    form_class = RegisterPresentationForm
    template_name = 'conferences/register_presentation.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        conference = get_object_or_404(Conference, pk=self.kwargs['pk'])
        context['conference'] = conference
        return context

    def form_valid(self, form):
        conference = get_object_or_404(Conference, pk=self.kwargs['pk'])
        presentation = form.save(commit=False)
        presentation.author = self.request.user
        presentation.conference = conference
        presentation.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('conference_detail', kwargs={'pk': self.kwargs['pk']})


class CancelPresentationView(LoginRequiredMixin, DeleteView):
    model = Presentation
    template_name = 'conferences/cancel_presentation.html'
    context_object_name = 'presentation'

    def get_object(self, queryset=None):
        presentation = get_object_or_404(Presentation, pk=self.kwargs['presentation_id'])
        return presentation

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        conference = get_object_or_404(Conference, pk=self.kwargs['conference_id'])
        context['conference'] = conference
        return context
    
    def get_success_url(self):
        return reverse_lazy('conference_detail', kwargs={'pk': self.kwargs['conference_id']})


class EditPresentationView(LoginRequiredMixin, UpdateView):
    model = Presentation
    fields = ['title', 'description']
    template_name = 'conferences/edit_presentation.html'
    context_object_name = 'presentation'

    def get_object(self, queryset=None):
        presentation = get_object_or_404(Presentation, pk=self.kwargs['presentation_id'])
        return presentation
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        conference = get_object_or_404(Conference, pk=self.kwargs['conference_id'])
        context['conference'] = conference
        return context

    def get_success_url(self):
        return reverse_lazy('conference_detail', kwargs={'pk': self.kwargs['conference_id']})


class ReviewsListView(LoginRequiredMixin, ListView):
    model = Review
    template_name = 'conferences/reviews_list.html'
    context_object_name = 'reviews'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        conference = get_object_or_404(Conference, pk=self.kwargs['conference_id'])
        context['conference'] = conference
        return context


class AddReviewView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['rating', 'text']
    template_name = 'conferences/add_review.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        conference = get_object_or_404(Conference, pk=self.kwargs['conference_id'])
        context['conference'] = conference
        return context

    def form_valid(self, form):
        conference = get_object_or_404(Conference, pk=self.kwargs['conference_id'])
        review = form.save(commit=False)
        review.user = self.request.user
        review.conference = conference
        review.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('reviews_list', kwargs={'conference_id': self.kwargs['conference_id']})
