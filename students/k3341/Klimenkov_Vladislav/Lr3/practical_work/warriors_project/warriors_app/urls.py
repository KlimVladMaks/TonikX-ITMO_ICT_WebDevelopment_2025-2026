from django.urls import path
from .views import (
    WarriorListAPIView, 
    WarriorCreateAPIView,
    WarriorRetrieveAPIView,
    WarriorUpdateAPIView,
    WarriorDestroyAPIView,
    SkillListAPIView, 
    SkillCreateAPIView,
    SkillRetrieveAPIView,
    SkillUpdateAPIView,
    SkillDestroyAPIView,
)

urlpatterns = [
    path('warriors/', WarriorListAPIView.as_view()),
    path('warriors/create/', WarriorCreateAPIView.as_view()),
    path('warriors/<int:pk>/', WarriorRetrieveAPIView.as_view()),
    path('warriors/<int:pk>/update/', WarriorUpdateAPIView.as_view()),
    path('warriors/<int:pk>/delete/', WarriorDestroyAPIView.as_view()),
    path('skills/', SkillListAPIView.as_view()),
    path('skills/create/', SkillCreateAPIView.as_view()),
    path('skills/<int:pk>/', SkillRetrieveAPIView.as_view()),
    path('skills/<int:pk>/update/', SkillUpdateAPIView.as_view()),
    path('skills/<int:pk>/delete/', SkillDestroyAPIView.as_view()),
]
