from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BusTypeViewSet,
    BusViewSet,
    RouteViewSet,
    DriverViewSet,
    DriverAssignmentViewSet,
    BusStatusViewSet,
    RouteDriversAPIView,
)

router = DefaultRouter()
router.register('bus-types', BusTypeViewSet)
router.register('buses', BusViewSet)
router.register('routes', RouteViewSet)
router.register('drivers', DriverViewSet)
router.register('driver-assignments', DriverAssignmentViewSet)
router.register('bus-statuses', BusStatusViewSet)

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include(router.urls)),
    path('routes/<int:route_id>/drivers/', RouteDriversAPIView.as_view())
]
