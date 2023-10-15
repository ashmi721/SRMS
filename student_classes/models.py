from django.db import models

# Create your models here.
class StudentClass(models.Model):
    class_name = models.IntegerField(help_text='Eg- 1,2,4,5 etc')
    section    =   models.CharField(max_length=10, help_text='Eg- A,B,C etc')
    creation_date =   models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    # def __str__(self):
    #     return self.class_name
    
    def get_class_name_display(self):
        class_names = {
           
        }
        return class_names.get(self.class_name, str(self.class_name))

    def __str__(self):
        return f"{self.get_class_name_display()}  {self.section}"