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
    Сериализатор для типа автобуса.
    """
    class Meta:
        model = BusType
        fields = '__all__'


class BusSerializer(serializers.ModelSerializer):
    """
    Сериализатор для автобуса.
    """
    class Meta:
        model = Bus
        fields = '__all__'


class RouteSerializer(serializers.ModelSerializer):
    """
    Сериализатор для маршрута.
    """
    class Meta:
        model = Route
        fields = '__all__'


class DriverSerializer(serializers.ModelSerializer):
    """
    Сериализатор для водителя.
    """
    class Meta:
        model = Driver
        fields = '__all__'


class DriverAssignmentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для назначения водителя.
    """
    class Meta:
        model = DriverAssignment
        fields = '__all__'


# Статус автобуса в конкретный день
class BusStatusSerializer(serializers.ModelSerializer):
    """
    Сериализатор для статуса автобуса.
    """
    class Meta:
        model = BusStatus
        fields = '__all__'
