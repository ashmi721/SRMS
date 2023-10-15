from django.db import models
from student_classes.models import StudentClass
from django.utils import timezone

# Create your models here.
class Student(models.Model):
   select_gender = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
   student_roll = models.IntegerField(unique=True)
   student_name = models.CharField(max_length=100)
   student_class = models.ForeignKey(StudentClass,on_delete=models.CASCADE)
   student_address = models.CharField(max_length=100)
   student_email = models.EmailField(blank=True, null=True)
   student_contact = models.CharField(max_length=14)
   student_gender = models.CharField(max_length=8, choices=select_gender)
   student_dob = models.DateTimeField(default=timezone.now)
   parents_name = models.CharField(max_length=30, blank=True, null=True)
   student_reg = models.DateField(auto_now_add=True)
   
   def __str__(self):
       return self.student_name
   
   
   