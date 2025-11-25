from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum, Avg, Count
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
    RouteDriversSerializer,
    TotalRouteLengthSerializer,
)


# ===== Базовые запросы =====


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


# ===== Специальные запросы =====

class RouteDriversAPIView(APIView):
    """
    Список водителей, работающих на определённом маршруте с указанием графика их работы.
    """
    def get(self, request, route_id):
        # Получаем маршрут
        try:
            route = Route.objects.get(pk=route_id)
        except Route.DoesNotExist:
            return Response(
                {"error": "Маршрут не найден"}, 
                status=status.HTTP_404_NOT_FOUND
            )

        # Получаем всех водителей, для которых этот маршрут является основным
        drivers = Driver.objects.filter(main_route=route).distinct()

        # Преобразуем данные в JSON
        serializer = RouteDriversSerializer({
            'route': route,
            'drivers': drivers
        })

        # Возвращаем данные
        return Response(serializer.data)


class TotalRouteLengthAPIView(APIView):
    """
    Общая протяжённость всех маршрутов.
    """
    def get(self, request):
        aggregation = Route.objects.aggregate(
            total_length=Sum('duration'),
            routes_count=Count('id'),
            average_length=Avg('duration')
        )
        if aggregation['total_length'] is None:
            aggregation['total_length'] = 0
            aggregation['routes_count'] = 0
            aggregation['average_length'] = 0
        serializer = TotalRouteLengthSerializer(aggregation)
        return Response(serializer.data, status=status.HTTP_200_OK)
