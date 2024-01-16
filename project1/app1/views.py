from django.shortcuts import render
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class Show_view(APIView):
    def get(self,request):
        data = Student.objects.all()
        serialize_data = StudentSerializer(data,many=True)
        return Response(serialize_data.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serialize_data = StudentSerializer(data=request.data)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response(serialize_data.data,status=status.HTTP_201_CREATED)


    