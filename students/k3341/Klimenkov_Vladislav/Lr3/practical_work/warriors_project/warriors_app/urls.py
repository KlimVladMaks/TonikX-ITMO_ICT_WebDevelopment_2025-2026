from django.urls import path
from .views import (WarriorsAPIView,
                    WarriorDetailAPIView)

urlpatterns = [
   path('warriors/', WarriorsAPIView.as_view()),
   path('warriors/<int:pk>/', WarriorDetailAPIView.as_view()),
]
