from django.db import models

# Create your models here.


class Employee(models.Model) :
    name = models.CharField('name',max_length=255)
    email =  models.EmailField(max_length=255)
    department = models.CharField('department', max_length=100)
    is_active = models.BooleanField (default = True)
    created_at = models.DateTimeField (auto_now_add = True)
    updated_at = models. DateTimeField (auto_now = True)

    def __str__(self):
        return  self.name
