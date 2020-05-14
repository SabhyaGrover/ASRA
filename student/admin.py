from django.contrib import admin
from .models import Student
# Register your models here.

#class StudentAdmin(admin.ModelAdmin):
#fieldsets = [
 #       ("Name",{'fields':["Student.name"]}),
  #      ("Age",{'fields':["Student.age"]}),
   #     ("Gender",{'fields':["Student.sex"]}),
    #    ("Date Of Admission",{'fields':["Student.date_of_admission"]}),
     ##  ("Height",{'fields':["Student.height"]})

#    ]

admin.site.register(Student)
