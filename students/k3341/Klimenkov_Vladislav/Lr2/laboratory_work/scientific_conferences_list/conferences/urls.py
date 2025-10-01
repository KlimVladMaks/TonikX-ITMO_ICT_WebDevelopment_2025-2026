from django.urls import path
from .views import ConferencesList

urlpatterns = [
    path('list/', ConferencesList.as_view(), name='conferences_list'),
]
