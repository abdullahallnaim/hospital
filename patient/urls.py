# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserRegistrationAPIView, UserLogoutAPIView, activate,UserLoginAPIView,UserDetailsAPIView, PatientViewSet
router = DefaultRouter()
router.register(r'list', PatientViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('register/', UserRegistrationAPIView.as_view(), name="register"),
    path('login/', UserLoginAPIView.as_view(), name="login"),
    path('logout/', UserLogoutAPIView.as_view()),
]
# urls.py

