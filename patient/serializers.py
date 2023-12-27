# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from . import models

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Patient
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True)  # New field
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email', 'password', 'confirm_password')
    def save(self):
        username = self.validated_data['username']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']
        
        if password != password2:
            raise serializers.ValidationError({'error': 'password does not matched'})
        if User.objects.filter(email = email).exists():
            raise serializers.ValidationError({'error': 'email already exists'})
        account = User(username= username, email = email)
        account.set_password(password)
        account.save()
        return account
        
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    # def validate(self, data):
    #     username = data.get('username')
    #     password = data.get('password')

    #     if username and password:
    #         user = User.objects.filter(username=username).first()

    #         if user and user.check_password(password):
    #             data['user'] = user
    #             return data
    #         else:
    #             raise serializers.ValidationError("Incorrect username or password.")
    #     else:
    #         raise serializers.ValidationError("Must include 'username' and 'password'.")
