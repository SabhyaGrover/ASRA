from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import (
    CreateView,
    ListView
)
from .models import Student,Job
from .forms import StudentForm,JobForm
from django.urls import reverse_lazy
# Create your views here.
def home(request):
    return render(request = request,template_name="student/dashboard.html")

def load_profile(reqeust):
    return render(request = request,template_name="student/profile_dropdown.html")

class ShowList(ListView):
    model = Student
    template_name = 'student/table.html'
    context_object_name = 'students'
    ordering = ['-date_of_admission']

class AddStudent(CreateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('student:table')

class AddJob(CreateView):
    model = Job
    form_class = JobForm
    success_url = reverse_lazy('student:test-job')

class ShowJob(ListView):
    model = Job
    template_name = 'student/test-job.html'
    context_object_name = 'jobs'