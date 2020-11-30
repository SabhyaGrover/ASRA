from django import forms
from .models import Student,Job,Marriage

class StudentForm(forms.ModelForm):
    class Meta:
        model= Student
        fields=('name','age','sex','date_of_admission','date_of_leaving','education', 'height')

class JobForm(forms.ModelForm):
    class Meta:
        model= Job
        fields=('student','preferred_location','date_of_joining','future_preferences','job_timings')
class MarriageForm(forms.ModelForm):
    class Meta:
        model= Marriage
        fields=('student','job','ailments','preferences', 'status')
