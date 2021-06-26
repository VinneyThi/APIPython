from django.db import models

# Create your models here.


class Employee(models.Model) :
    name = models.CharField('name',max_length=255)
    email =  models.EmailField(max_length=255)
    department = models.CharField('department', max_length=100)

