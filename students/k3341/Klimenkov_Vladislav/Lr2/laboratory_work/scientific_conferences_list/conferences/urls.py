from django.urls import path
from .views import ConferencesListView, ConferenceDetailView


urlpatterns = [
    path('list/', ConferencesListView.as_view(), name='conferences_list'),
    path('<int:pk>/', ConferenceDetailView.as_view(), name='conference_detail'),
]
