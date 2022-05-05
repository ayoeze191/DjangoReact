import email
from email.headerregistry import Address
from unicodedata import name
from django.shortcuts import render
from django.conf import settings
import random
import string
from datetime import datetime, timedelta
from django.contrib.auth import authenticate
# Create your views here.
from rest_framework.views import APIView
from .serializer import TeacherCreationSerializer, LoginSerializer, UserSerializer, LogOutTokenSerializers
from rest_framework.response import Response
from .models import CustomUser, Teacher, Jwt, TeachersBankDetails
import jwt




def get_random(length):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
def get_access_token(payload):
    return jwt.encode({'exp':datetime.now() + timedelta(hours=5), **payload}, 
    settings.SECRET_KEY, algorithm="HS256")


def get_refresh_token():
    return jwt.encode(
        {"exp": datetime.now() + timedelta(days=365), "data":get_random(10)},
         settings.SECRET_KEY, algorithm="HS256"
    )



class TeacherRegistrationViews(APIView):
    def post(self, request):
        data = request.data
        serializer = TeacherCreationSerializer(data = data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        CustomUser.objects._create_(is_teacher = True, email = serializer.validated_data['email'], name = serializer.validated_data['first_name'], password = serializer.validated_data['password'])
        teacher = CustomUser.objects.get(email=serializer.validated_data['email'])
        teacher_details = Teacher(
            user = teacher, 
            first_name = serializer.validated_data['email'],
             Surname = serializer.validated_data['Surname'], 
             phone_number = serializer.validated_data['phone_number'],
             Gender = serializer.validated_data['Gender'],
             Address = serializer.validated_data['Address'],
             Date_of_birth = serializer.validated_data['Date_of_birth'],
             state_of_residence = serializer.validated_data['state_of_residence'],
             disability = serializer.validated_data['disability'],
             About_Teacher = serializer.validated_data['About_Teacher'],
             Facebook = serializer.validated_data['Facebook'],
            instagram = serializer.validated_data['instagram'],
            Twitter = serializer.validated_data['Twitter'],
             )
        
        teacher_details.save()
        
        return Response({"succecfully created"})


class TeacherLoginView(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username = serializer.validated_data['email'], password = serializer.validated_data['password'])
        if not user:
            return Response({"invalid: username"}, status=400)
        Jwt.objects.filter(user_id=user.id).delete()
        access = get_access_token({"user_id": user.id, "username": user.get_username()})
        print('access', access)
        refresh = get_refresh_token()
        serializedUser = UserSerializer(user)
        Jwt.objects.create(
            user_id = user.id, access=access, refresh=refresh
        )
        return Response({'access': access, 'refresh': refresh, 'user': serializedUser.data})


class LogoutView(APIView):
    serializer_class = LogOutTokenSerializers
    def get(self, request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data['access']
        try:
            Jwt.objects.get(access = serializer.validated_data['access'])
        except Jwt.DoesNotExist:
            return Response({"data": "invalid token"})
        else:
            Jwt.objects.get(access=serializer.validated_data["access"]).delete()
            return Response({"logged out successfully"})


