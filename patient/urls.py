# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import UserRegistrationAPIView, UserLogoutAPIView, activate,UserLoginAPIView,UserDetailsAPIView
# router = DefaultRouter()
# router.register(r'users', UserViewSet)
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    # path('', include(router.urls)),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('register/', UserRegistrationAPIView.as_view(), name="register"),
    path('login/', UserLoginAPIView.as_view(), name="login"),
    path('logout/', UserLogoutAPIView.as_view()),
]
# urls.py

