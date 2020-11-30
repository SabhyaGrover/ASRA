from django.urls import path
from . import views
from .views import (
AddStudent,
ShowList,
ShowJob,
AddJob,
AddMarriage,
ShowMarriageList
)
app_name = 'student'

urlpatterns = [
    path('',views.home, name='home'),
    path('add/',AddStudent.as_view(), name='add'),
    path('view/',ShowList.as_view(), name='table'),
    path('add-job/',AddJob.as_view(), name='add-job'),
    path('view-job/',ShowJob.as_view(), name='view-job'),
    path('add-marriage',AddMarriage.as_view(), name='add-marriage'),
    path('view-marriage',ShowMarriageList.as_view(), name='view-marriage')
]
