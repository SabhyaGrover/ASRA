from django.urls import path
from . import views
from .views import (
AddStudent,
ShowList
)
app_name = 'student'

urlpatterns = [
    path('',views.home, name='home'),
    path('add/',AddStudent.as_view(), name='add'),
    path('view/',ShowList.as_view(), name='table'),
]