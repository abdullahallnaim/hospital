# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import UserRegistrationAPIView, Logout, activate,UserLoginAPIView, PatientViewSet
from rest_framework.authtoken.views import obtain_auth_token
router = DefaultRouter()
router.register('', PatientViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('register/', UserRegistrationAPIView.as_view(), name="register"),
    path('login/', UserLoginAPIView.as_view(), name="login"),
    path('logout/', Logout.as_view()),
]
# urls.py

