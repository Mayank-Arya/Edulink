from django.shortcuts import render
from rest_framework import generics
from .models import Course
from .serializers import CourseSerializer

# courses/views.py

from departments.models import Department  # Check this import

class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
