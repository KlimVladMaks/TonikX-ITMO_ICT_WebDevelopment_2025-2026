from django.urls import path
from .views import (ConferencesListView, 
                    ConferenceDetailView, 
                    RegisterPresentationView,
                    CancelPresentationView)


'''
# Примечание:

Параметр `pk` в conference_detail используется в
`reverse_lazy('conference_detail', kwargs={'pk': self.kwargs['conference_id']})`
в CancelPresentationView.

Изменение названия с `pk` на другое может привести к ошибкам.
'''
urlpatterns = [
    path('list/', ConferencesListView.as_view(), name='conferences_list'),
    path('<int:pk>/', ConferenceDetailView.as_view(), name='conference_detail'),
    path('<int:pk>/register-presentation/',
         RegisterPresentationView.as_view(), 
         name='register_presentation'),
    path('<int:conference_id>/presentations/<int:presentation_id>/cancel',
         CancelPresentationView.as_view(),
         name='cancel_presentation'),
]
