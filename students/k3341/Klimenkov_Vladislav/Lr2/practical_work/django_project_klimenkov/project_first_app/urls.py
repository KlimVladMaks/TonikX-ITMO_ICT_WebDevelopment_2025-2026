from django.urls import path
from . import views


urlpatterns = [
    path('owner/<int:id>/', views.owner_detail, name='owner_detail'),
]
