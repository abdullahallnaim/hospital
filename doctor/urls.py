from django.urls import include, path
from rest_framework import routers
from .views import DoctorViewSet,  AvailableTimeViewSet,DesignationViewSet,SpecializationViewSet

router = routers.DefaultRouter()
router.register('list', DoctorViewSet)
router.register('doctors_time', AvailableTimeViewSet)
router.register('designation', DesignationViewSet)
router.register('specialization', SpecializationViewSet)
router.register('availabletime', AvailableTimeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # # path('api_auth/', include('rest_framework.urls')),
    # path('doctor/<int:doctor_id>/', DoctorAvailableTimeView.as_view(), name='doctor-available-time'),
]