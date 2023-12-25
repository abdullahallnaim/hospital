from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
# from . import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# from . import paginations
from rest_framework.generics import ListAPIView
from . import models
from rest_framework import filters

from rest_framework import viewsets, pagination
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorPagination(pagination.PageNumberPagination):
    page_size = 1  # Define the number of items per page
    page_size_query_param = 'page_size'
    max_page_size = 100
    
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = models.Doctor.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__first_name','specialization__name', 'designation__name']
    serializer_class = serializers.DoctorSerializer
    pagination_class = DoctorPagination

class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = models.Specialization.objects.all()
    serializer_class = serializers.SpecializationSerializer

class AvailableTimeViewSet(viewsets.ModelViewSet):
    queryset = models.AvailableTime.objects.all()
    serializer_class = serializers.AvailableTimeSerializer
    
class DesignationViewSet(viewsets.ModelViewSet):
    queryset = models.Designation.objects.all()
    serializer_class = serializers.DesignationSerializer
