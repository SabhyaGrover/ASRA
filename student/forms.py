from django import forms
from .models import Student, Marriage

class StudentForm(forms.ModelForm):
    class Meta:
        model= Student
        fields=('name','age','sex','date_of_admission','date_of_leaving','education', 'height')

class MarriageForm(forms.ModelForm):
    class Meta:
        model= Marriage
        fields=('student','job','ailments','preferences', 'status')
