from django.urls import path
from . import views
from .views import (
AddStudent,
ShowList,
AddMarriage,
ShowMarriageList
)
app_name = 'student'

urlpatterns = [
    path('',views.home, name='home'),
    path('add/',AddStudent.as_view(), name='add'),
    path('view/',ShowList.as_view(), name='table'),
    path('marriageform/',AddMarriage.as_view(), name='marriage-add'),
    path('marriageview/',ShowMarriageList.as_view(), name='marriage-view')
]
