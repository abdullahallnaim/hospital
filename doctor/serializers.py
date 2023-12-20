from rest_framework import serializers, viewsets
from .models import Doctor, Designation, Department, AvialableTimeForDoctor, Specialization, ScheduleTime

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'
class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'
class AvailableTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvialableTimeForDoctor
        fields = '__all__'
class ScheduleTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleTime
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    designation = serializers.StringRelatedField(many=True)
    specialization = serializers.StringRelatedField(many=True)
    department = serializers.StringRelatedField(many=False)
    class Meta:
        model = Doctor
        fields = '__all__'
