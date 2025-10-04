from django.urls import path
from .views import ConferencesListView, ConferenceDetailView, RegisterPresentationView


urlpatterns = [
    path('list/', ConferencesListView.as_view(), name='conferences_list'),
    path('<int:pk>/', ConferenceDetailView.as_view(), name='conference_detail'),
    path('<int:pk>/register-presentation/',
         RegisterPresentationView.as_view(), 
         name='register_presentation')
]
