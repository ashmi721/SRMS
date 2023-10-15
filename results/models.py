from django.db import models
from student_classes.models import StudentClass
from students.models import Student
# from django.contrib.postgres.fields import JSONField
# Create your models here.
class DisplayResult(models.Model):
    select_class = models.ForeignKey(StudentClass,on_delete=models.CASCADE)
    select_student = models.ForeignKey(Student,on_delete=models.CASCADE)
  
    
    def __str__(self):
        return "%s Section-%s" % (self.select_class.class_name, self.select_class.section)
