from django.urls import path
from .views import (
    WarriorListAPIView, 
    WarriorCreateAPIView,
    WarriorRetrieveAPIView,
    WarriorUpdateAPIView,
    WarriorDestroyAPIView
)

urlpatterns = [
    path('warriors/', WarriorListAPIView.as_view()),
    path('warriors/create/', WarriorCreateAPIView.as_view()),
    path('warriors/<int:pk>/', WarriorRetrieveAPIView.as_view()),
    path('warriors/<int:pk>/update/', WarriorUpdateAPIView.as_view()),
    path('warriors/<int:pk>/delete/', WarriorDestroyAPIView.as_view()),
]
