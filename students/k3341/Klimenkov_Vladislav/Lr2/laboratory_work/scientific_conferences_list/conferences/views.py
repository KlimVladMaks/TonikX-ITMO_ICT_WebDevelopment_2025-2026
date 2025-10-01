from django.views.generic import ListView
from .models import Conference


class ConferencesList(ListView):
    model = Conference
    template_name = 'conferences/conferences_list.html'
    context_object_name = 'conferences'
    paginate_by = 10
