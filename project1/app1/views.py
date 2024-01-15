from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def show_view(request):
    data = Student.objects.all()
    serialize_data = StudentSerializer(data,many=True)
    return Response(serialize_data.data)
