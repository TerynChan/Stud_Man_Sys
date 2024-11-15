from django.db import models

import student


# Create your models here.

class Student(models.Model):
  student_number = models.PositiveIntegerField()
  image = models.ImageField( default = "placeholder.png", upload_to='images/')
  firstname = models.CharField(max_length=50)
  lastname = models.CharField(max_length=50)
  email = models.EmailField(max_length=100)
  program = models.CharField(max_length=50)
  
  def __str__(self) -> str:
        return f"{self.id}: {self.firstname} {self.lastname}  "
   

    
    


