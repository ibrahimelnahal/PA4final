from django import forms

from PA3.models import *


class StudentForm(forms.Form):
    first_name=forms.CharField(max_length=30)
    last_name=forms.CharField(max_length=30)
    email = forms.EmailField()
    #courses = models.ManyToManyField(Course)



class TeacherForm(forms.Form):
    first_name=forms.CharField(max_length=30)
    last_name=forms.CharField(max_length=30)
    office=forms.CharField(max_length=15)
    email = forms.EmailField()
    phone=forms.CharField(max_length=13)



class CourseForm(forms.Form):
    name = forms.CharField(max_length=30)
    code = forms.CharField(max_length=6)
    time=forms.TimeField()
    classroom=forms.CharField(max_length=6)
    teacher = forms.ModelChoiceField(queryset = Teacher.objects.all())
    #students = forms.ManyToManyField(Student)



