from django.urls import path
from .views import ConferencesListView


urlpatterns = [
    path('list/', ConferencesListView.as_view(), name='conferences_list'),
]
