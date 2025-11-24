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


# Тип автобуса
class BusTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusType
        fields = '__all__'


# Автобус
class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = '__all__'


# Маршрут
class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'


# Водитель
class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'


# Назначение водителя на автобус в конкретный день
class DriverAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverAssignment
        fields = '__all__'


# Статус автобуса в конкретный день
class BusStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusStatus
        fields = '__all__'
