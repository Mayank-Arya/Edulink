from django.shortcuts import render
from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import DestroyAPIView


class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentUpdateView(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDeleteView(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer