from rest_framework import serializers
from .models import (
    BusType,
    Bus,
    Route,
    Driver,
    DriverAssignment,
    BusStatus,
)


# ==== Базовые сериализаторы =====


class BusTypeSerializer(serializers.ModelSerializer):
    """
    Базовый сериализатор для типа автобуса.
    """
    class Meta:
        model = BusType
        fields = '__all__'


class BusSerializer(serializers.ModelSerializer):
    """
    Базовый сериализатор для автобуса.
    """
    class Meta:
        model = Bus
        fields = '__all__'


class RouteSerializer(serializers.ModelSerializer):
    """
    Базовый сериализатор для маршрута.
    """
    class Meta:
        model = Route
        fields = '__all__'


class DriverSerializer(serializers.ModelSerializer):
    """
    Базовый сериализатор для водителя.
    """
    class Meta:
        model = Driver
        fields = '__all__'


class DriverAssignmentSerializer(serializers.ModelSerializer):
    """
    Базовый сериализатор для назначения водителя.
    """
    class Meta:
        model = DriverAssignment
        fields = '__all__'


class BusStatusSerializer(serializers.ModelSerializer):
    """
    Базовый сериализатор для статуса автобуса.
    """
    class Meta:
        model = BusStatus
        fields = '__all__'


# ===== Сериализаторы для специальных запросов =====


class DriverWithAssignmentsSerializer(serializers.ModelSerializer):
    """
    Сериализатор для водителя с его назначениями.
    """
    assignments = serializers.SerializerMethodField()

    class Meta:
        model = Driver
        fields = '__all__'
    
    def get_assignments(self, obj):
        assignments = DriverAssignment.objects.filter(driver=obj)
        return DriverAssignmentSerializer(assignments, many=True).data


class RouteDriversSerializer(serializers.Serializer):
    """
    Сериализатор для маршрута с водителями и их графиком работы.
    """
    route = RouteSerializer()
    drivers = DriverWithAssignmentsSerializer(many=True)


class TotalRouteLengthSerializer(serializers.Serializer):
    """
    Сериализатор для общей протяжённости маршрутов.
    """
    total_length = serializers.IntegerField()
    routes_count = serializers.IntegerField()
    average_length = serializers.FloatField()


class BusStatusDetailSerializer(serializers.ModelSerializer):
    """
    Сериализатор для статуса автобуса с детальной информацией об автобусе.
    """
    bus = BusSerializer(read_only=True)
    class Meta:
        model = BusStatus
        fields = '__all__'
