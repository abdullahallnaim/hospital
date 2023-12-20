from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
# from . import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# from . import paginations

class AppointmentViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.AdminOrReadOnly]
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializer