from django.urls import path
from .views import StudentListCreateView, StudentDetailView, StudentUpdateView, StudentDeleteView, CustomLoginView

urlpatterns = [
    # URL pattern for listing and creating students
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('students/<int:pk>', StudentDetailView.as_view(), name='student-detail'),
     path('students/<int:pk>', StudentUpdateView.as_view(), name='student-update'),
     path('students/<int:pk>', StudentDeleteView.as_view(), name='student-delete'),
      path('students/login/', CustomLoginView.as_view(), name='login'),
]