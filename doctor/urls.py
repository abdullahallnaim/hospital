from django.urls import include, path
from rest_framework import routers
from .views import DoctorViewSet, DepartmentViewSet, AvailableTimeViewSet,DesignationViewSet,SpecializationViewSet, ScheduleTimeViewSet,DoctorAvailableTimeView

router = routers.DefaultRouter()
router.register('doctors', DoctorViewSet)
router.register('departments', DepartmentViewSet)
router.register('doctors_time', AvailableTimeViewSet)
router.register('designation', DesignationViewSet)
router.register('specialization', SpecializationViewSet)
router.register('scheduletime', ScheduleTimeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('api_auth/', include('rest_framework.urls')),
    path('doctor/<int:doctor_id>/', DoctorAvailableTimeView.as_view(), name='doctor-available-time'),
]