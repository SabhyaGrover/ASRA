from django.urls import path
from . import views
from .views import (
AddStudent,
ShowList,
ShowJob,
AddJob
)
app_name = 'student'

urlpatterns = [
    path('',views.home, name='home'),
    path('add/',AddStudent.as_view(), name='add'),
    path('view/',ShowList.as_view(), name='table'),
    path('add-job/',AddJob.as_view(), name='add-job'),
    path('test-job/',ShowJob.as_view(), name='test-job')
]