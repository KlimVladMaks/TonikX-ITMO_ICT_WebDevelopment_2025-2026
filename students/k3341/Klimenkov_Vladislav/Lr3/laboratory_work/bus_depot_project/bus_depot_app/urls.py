from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BusTypeViewSet
)

router = DefaultRouter()
router.register('bus-types', BusTypeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
