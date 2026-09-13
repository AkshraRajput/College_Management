from django.urls import path
from students import views

urlpatterns = [
    path("", views.student_home),
    path("profile/", views.student_profile),
    path("courses/", views.student_courses),
]