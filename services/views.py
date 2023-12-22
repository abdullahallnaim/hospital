from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers
# Create your views here.
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer