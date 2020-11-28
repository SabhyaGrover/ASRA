from django.db import models
from datetime import date
from django.contrib.auth.models import User
import datetime
from django.urls import reverse
# Create your models here.
class Student(models.Model):
    GENDER =(
        ('M','Male'),
        ('F','Female'),
    )
    EDUCATION = (
        ('10','10th Pass'),
        ('12','12th Pass'),
        ('D','Diploma'),
    )
    #stid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    sex = models.CharField(max_length=1,default=('F'),choices=GENDER)
    date_of_admission = models.DateField(default=date.today())
    date_of_leaving = models.DateField(null=True,blank=True)
    education = models.CharField(max_length=30,choices=EDUCATION)
    height = models.IntegerField(help_text='Please enter height in cms')

    def get_absolute_url(self):
        return reverse('student:table')

class Marriage(models.Model):
    student = models.OneToOneField(Student,on_delete=models.CASCADE)
    ailments = models.CharField(blank=True,max_length=100)
    job = models.CharField(max_length=20,blank=True)
    preferences = models.TextField(default=' ')
    status =  models.BooleanField()

class Job(models.Model):
    student = models.OneToOneField(Student,on_delete=models.CASCADE)
    preferred_location = models.TextField(default=' ')
    date_of_joining = models.DateField(default=date(1000, 1, 1))
    #qualification
    future_preferences = models.TextField()
    job_timings = models.TextField()
    def get_absolute_url(self):
        return reverse('student:test-job')