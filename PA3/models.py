from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Student(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email = models.EmailField()

class Teacher(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    office=models.CharField(max_length=15)
    email = models.EmailField()
    phone=models.CharField(max_length=13)


class Course(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=6)
    time=models.TimeField()
    classroom=models.CharField(max_length=6)
    teacher = models.ForeignKey(Teacher)
    # students = models.ManyToManyField(Student)



