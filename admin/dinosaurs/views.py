from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import DinosaurSerializer
from .models import Dinosaur
from .producer import publish


# Create your views here.
class DinosaurViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Dinosaur.objects.all()
    serializer_class = DinosaurSerializer

    @action(detail=False, methods=['POST'])
    def add(self, request, pk=None):
        serializer = DinosaurSerializer(data=request.data)
        if serializer.is_valid():
            result = serializer.save()
            response = {'success': True, 'data': DinosaurSerializer(result).data,
                        'message': 'a new dinosaurs is added'}
            publish('DinosaurCreated', serializer.data)
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
