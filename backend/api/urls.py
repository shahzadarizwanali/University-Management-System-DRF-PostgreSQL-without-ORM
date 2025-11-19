from django.urls import path
from .views import (
    university,
    university_detail,
    department,
    department_detail,
    faculty,
    faculty_detail,
    student,
    student_detail,
    classroom,
    classroom_detail,
)

urlpatterns = [
    path("university/", university),
    path("university/<int:id>", university_detail),
    path("departments/", department),
    path("departments/<int:id>", department_detail),
    path("faculty/", faculty),
    path("faculty/<int:id>", faculty_detail),
    path("students/", student),
    path("students/<int:id>", student_detail),
    path("classrooms/", classroom),
    path("classrooms/<int:id>", classroom_detail),
]
