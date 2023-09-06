from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('inst/', views.InstructorListCreateView.as_view(), name='instructor-list-create'),
    path('inst/<int:pk>/', views.InstructorDetailView.as_view(), name='instructor-detail'),
]
