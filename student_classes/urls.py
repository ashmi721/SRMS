from django.urls import path
from student_classes.views import home

urlpatterns = [
    path("",home),
]
