from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/students/', include('students.urls')),  # Include the students' URLs
    path('api/instructors/', include('instructors.urls')),  # Include the instructors' URLs
    path('api/courses/', include('courses.urls')),
    path('api/dept/', include('departments.urls'))
]
