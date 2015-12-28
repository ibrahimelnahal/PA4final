# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from PA3.forms import StudentForm, TeacherForm, CourseForm
from PA3.models import Student, Teacher, Course



def addTeacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            a = Teacher(first_name=form.cleaned_data["first_name"],
                       last_name=form.cleaned_data["last_name"],
                       office=form.cleaned_data["office"],
                       email=form.cleaned_data["email"],
                       phone=form.cleaned_data["phone"],)
            a.save()
            return HttpResponseRedirect('/all-Teachers/')
    else:
        form = TeacherForm()
    return render_to_response('addTeacher.html', {'form': form}, RequestContext(request))


def addStudnet(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            a = Student(first_name=form.cleaned_data["first_name"],
                       last_name=form.cleaned_data["last_name"],
                       email=form.cleaned_data["email"])
            a.save()
            return HttpResponseRedirect('/all-Students/')
    else:
        form = StudentForm()
    return render_to_response('addStudent.html', {'form': form}, RequestContext(request))



def addCourse(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            a = Course(name=form.cleaned_data["name"],
                       code=form.cleaned_data["code"],
                       time=form.cleaned_data["time"],
                       classroom=form.cleaned_data["classroom"],
                       teacher=form.cleaned_data["teacher"])
            a.save()
            return HttpResponseRedirect('/all-Courses/')
    else:
        form = CourseForm()
    return render_to_response('addCourse.html', {'form': form}, RequestContext(request))

"""

def addstudnetincourse(request):
    if request.method == 'POST':
        form = studentincourseForm(request.POST)
        if form.is_valid():
            a = studentincourse(students=form.cleaned_data["students"],
                       courses=form.cleaned_data["courses"])
            a.save()
            return HttpResponseRedirect('/sall-Student/')
    else:
        form = studentincourseForm()
    return render_to_response('addstudnetincourse.html', {'form': form}, RequestContext(request))


"""
def all_Teachers(request):
    return render_to_response('all_Teachers.html', {'Teachers_list': Teacher.objects.all()})


def all_Students(request):
    return render_to_response('all_Students.html', {'Students_list': Student.objects.all()})


def all_Courses(request):
    return render_to_response('all_Courses.html', {'Courses_list': Course.objects.all()})
