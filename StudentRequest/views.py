from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from Account.models import Teacher
from .serializer import TutorSerializer

class AllTutors(APIView):
    def get(self, request):
        tutors = Teacher.objects.all()
        serializer = TutorSerializer(tutors, many= True)
        print(serializer.data)
        return Response(serializer.data)