from dataclasses import field, fields
import email
from rest_framework import serializers
from .models import Teacher

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    
class LogOutTokenSerializers(serializers.Serializer):
    access = serializers.CharField()

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField()
    is_staff = serializers.BooleanField()
    is_superuser = serializers.BooleanField()
    is_teacher = serializers.BooleanField()


class TeacherCreationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    Surname = serializers.CharField()
    phone_number = serializers.CharField()
    Gender = serializers.CharField()
    Address = serializers.CharField()
    Date_of_birth = serializers.DateField()
    state_of_residence = serializers.CharField()
    verified = serializers.BooleanField(default=False)
    disability = serializers.BooleanField()
    About_Teacher = serializers.CharField()
    Facebook = serializers.CharField()
    Twitter = serializers.CharField()
    instagram = serializers.CharField()


    
# class LogOutTokenSerializers(serializers.Serializer):
#     access = serializers.CharField()

# class RefreshTokenSerializers(serializers.Serializer):
#     # access = serializers.CharField()
#     refresh = serializers.CharField()



# class StudentRegisterSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField()
#     name = serializers.CharField()
#     last_name = serializers.CharField()

# class TeacherRegistrationSerializer(serializers.Serializer):




