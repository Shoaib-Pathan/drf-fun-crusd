from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def show_view(request,pk=None):
    id = pk
    if id is not None:
        data = Student.objects.get(id=id)
        serialize_data = StudentSerializer(data)
        return Response(serialize_data.data)
    data = Student.objects.all()
    serialize_data = StudentSerializer(data,many=True)
    return Response(serialize_data.data)

@api_view(['POST'])
def add_view(request):
    serialize_data = StudentSerializer(data=request.data)
    if serialize_data.is_valid():
        serialize_data.save()
        return Response(serialize_data.data)
    return Response(serialize_data.errors)

@api_view(['PUT'])
def update_view(request,pk=None):
    id = pk
    data = Student.objects.get(id=id)
    serialize_data = StudentSerializer(instance=data,data = request.data)
    if serialize_data.is_valid():
        serialize_data.save()
        return Response(serialize_data.data)

@api_view(['DELETE'])    
def delete_view(request,pk=None):
    id = pk
    data = Student.objects.get(id=id)
    data.delete()
    return Response('{msg:data deleted successully}')
    