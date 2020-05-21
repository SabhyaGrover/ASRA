from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import (
    CreateView,
    ListView
)
from .models import Student
from .forms import StudentForm
from django.urls import reverse_lazy
# Create your views here.
def home(request):
    return render(request = request,template_name="student/dashboard.html")

def add(request):
    if request.method =='POST':
        form = AddStudent(request.POST)
    return render(request = request, template_name="student/student.html")

def table(request):
    context = {
        "students": Student.objects.all()
    }
    return render(request,'student/tables.html',context)


class ShowList(ListView):
    model = Student
    template_name = 'student/table.html'
    context_object_name = 'students'
    ordering = ['-date_of_admission']

class AddStudent(CreateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('table')

