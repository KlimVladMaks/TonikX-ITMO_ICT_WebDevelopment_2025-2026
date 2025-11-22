from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Warrior
from .serializers import WarriorSerializer


class WarriorsAPIView(APIView):
    # GET - получение всех воинов
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorSerializer(warriors, many=True)
        return Response({"Warriors": serializer.data})

    # POST - создание нового воина
    def post(self, request):
        serializer = WarriorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WarriorDetailAPIView(APIView):
    # GET - получение одного воина по ID
    def get(self, request, pk):
        warrior = get_object_or_404(Warrior, pk=pk)
        serializer = WarriorSerializer(warrior)
        return Response(serializer.data)
    
    # PUT - полное обновление воина
    def put(self, request, pk):
        warrior = get_object_or_404(Warrior, pk=pk)
        serializer = WarriorSerializer(warrior, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # PATCH - частичное обновление воина
    def patch(self, request, pk):
        warrior = get_object_or_404(Warrior, pk=pk)
        serializer = WarriorSerializer(warrior, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # DELETE - удаление воина
    def delete(self, request, pk):
        warrior = get_object_or_404(Warrior, pk=pk)
        warrior.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class ProfessionCreateAPIView(APIView):
#    def post(self, request):
#        profession = request.data.get("profession")
#        serializer = ProfessionCreateSerializer(data=profession)
#        if serializer.is_valid(raise_exception=True):
#            profession_saved = serializer.save()
#        return Response({"Success": "Profession '{}' created successfully.".format(profession_saved.title)})
