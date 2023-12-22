from django.urls import include, path
from rest_framework import routers
from .views import ServiceViewSet

router = routers.DefaultRouter()
router.register('', ServiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]