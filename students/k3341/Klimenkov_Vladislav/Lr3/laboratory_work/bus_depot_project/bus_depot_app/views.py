from rest_framework import viewsets
from .models import (
    BusType,
    Bus,
    Route,
    Driver,
    DriverAssignment,
    BusStatus,
)
from .serializers import (
    BusTypeSerializer,
    BusSerializer,
    RouteSerializer,
    DriverSerializer,
    DriverAssignmentSerializer,
    BusStatusSerializer,
)


class BusTypeViewSet(viewsets.ModelViewSet):
    """
    ViewSet для типа автобуса.
    """
    serializer_class = BusTypeSerializer
    queryset = BusType.objects.all()


class BusViewSet(viewsets.ModelViewSet):
    """
    ViewSet для автобуса.
    """
    serializer_class = BusSerializer
    queryset = Bus.objects.all()


class RouteViewSet(viewsets.ModelViewSet):
    """
    ViewSet для маршрута.
    """
    serializer_class = RouteSerializer
    queryset = Route.objects.all()


class DriverViewSet(viewsets.ModelViewSet):
    """
    ViewSet для водителя.
    """
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()


class DriverAssignmentViewSet(viewsets.ModelViewSet):
    """
    ViewSet для назначения водителя.
    """
    serializer_class = DriverAssignmentSerializer
    queryset = DriverAssignment.objects.all()


class BusStatusViewSet(viewsets.ModelViewSet):
    """
    ViewSet для статуса автобуса.
    """
    serializer_class = BusStatusSerializer
    queryset = BusStatus.objects.all()
