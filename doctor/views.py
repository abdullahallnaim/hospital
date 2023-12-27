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
    
# class AvailableTimeViewSet(viewsets.ModelViewSet):
#     queryset = models.AvailableTime.objects.all()
#     serializer_class = serializers.AvailableTimeSerializer

from rest_framework import viewsets, filters


class AvailableTimeFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        doctor_id = request.query_params.get('doctor_id')  # Assuming doctor_id is passed as a query parameter
        if doctor_id:
            return queryset.filter(doctor=doctor_id)
        return queryset

class AvailableTimeViewSet(viewsets.ModelViewSet):
    queryset = models.AvailableTime.objects.all()
    serializer_class = serializers.AvailableTimeSerializer
    filter_backends = [AvailableTimeFilterBackend]
    
    
class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = models.Specialization.objects.all()
    serializer_class = serializers.SpecializationSerializer


    
    def get_queryset(self):
        queryset = super().get_queryset()
        doctor_id = self.request.query_params.get('doctor_id')
        print(doctor_id)
        if doctor_id:
            queryset = queryset.filter(doctor_id=doctor_id)
        return queryset
    
class DesignationViewSet(viewsets.ModelViewSet):
    queryset = models.Designation.objects.all()
    serializer_class = serializers.DesignationSerializer
    
    
class ReviewViewSet(viewsets.ModelViewSet):
    # queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    queryset = models.Review.objects.all()  # Retrieve all reviews by default

    def get_queryset(self):
        queryset = super().get_queryset()
        doctor_id = self.request.query_params.get('doctor_id')
        print(doctor_id)
        if doctor_id:
            queryset = queryset.filter(doctor_id=doctor_id)
        return queryset
