from rest_framework import generics
from .models import Warrior
from .serializers import WarriorSerializer


class WarriorListAPIView(generics.ListAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer


class WarriorCreateAPIView(generics.CreateAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer 


class WarriorRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer


class WarriorUpdateAPIView(generics.UpdateAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer


class WarriorDestroyAPIView(generics.DestroyAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer
