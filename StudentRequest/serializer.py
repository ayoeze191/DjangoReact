from dataclasses import field
from pyexpat import model
from rest_framework.serializers import ModelSerializer
from Account.models import Teacher

class TutorSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

    