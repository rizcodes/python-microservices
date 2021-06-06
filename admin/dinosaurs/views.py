from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DinosaurSerializer
from .models import Dinosaur


# Create your views here.
class DinosaurViewSet(viewsets.ModelViewSet):
    queryset = Dinosaur.objects.all()
    serializer_class = DinosaurSerializer
