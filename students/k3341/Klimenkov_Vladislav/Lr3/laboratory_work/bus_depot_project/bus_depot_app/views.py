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
    serializer_class = BusTypeSerializer
    queryset = BusType.objects.all()
