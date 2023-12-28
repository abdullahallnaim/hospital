# views.py
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserSerializer,UserLoginSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.sites.shortcuts import get_current_site
# verify email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User 

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from . import models
from . import serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters


class UserRegistrationAPIView(APIView):
    serializer_class = UserSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Generate email confirmation token
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            current_site = get_current_site(request)
            # Prepare and send email
            confirmation_link = f"https://testing-8az5.onrender.com/patient/activate/{uid}/{token}/"  # Replace with your confirmation URL
            email_subject = 'Confirm your email'
            email_body = render_to_string('register_email.html', {'confirmation_link': confirmation_link})

            email = EmailMultiAlternatives(
                email_subject, '', to=[user.email]
            )
            email.attach_alternative(email_body, "text/html")
            # send_email.send()
            email.send()

            return Response('Check your email for confirmation.', status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        # messages.error(request, 'Invalid activation link')
        return redirect('register')



class UserLoginAPIView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)

            if user:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key, 'user_id' : user.id})
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserDetailsAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user  # This will contain the authenticated user
        # You can serialize the user data as needed
        serialized_user_data = {
            'username': user.username,
            'email': user.email,
            # Add other user details you want to retrieve
        }
        return Response(serialized_user_data, status=status.HTTP_200_OK)
    
class UserLogoutAPIView(APIView):
    def post(self, request):
        try:
            # Get the user's token from the request headers
            token_key = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
            token = Token.objects.get(key=token_key)
            # Delete the token
            token.delete()
            return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
        except AttributeError:
            return Response({'error': 'Token not provided'}, status=status.HTTP_400_BAD_REQUEST)




# class PatientViewSet(filters.BaseFilterBackend):
#     # queryset = User.objects.all()
#     # serializer_class = serializers.PatientSerializer
    
#     def filter_queryset(self, request, queryset, view):
#         user_id = request.query_params.get('user_id')  # Assuming doctor_id is passed as a query parameter
#         if user_id:
#             return queryset.filter(user=user_id)
#         return queryset
    
class UserFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        user_id = request.query_params.get('user_id')  # Assuming doctor_id is passed as a query parameter
        if user_id:
            return queryset.filter(user=user_id)
        return queryset

class PatientViewSet(viewsets.ModelViewSet):
    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializer
    filter_backends = [UserFilterBackend]
