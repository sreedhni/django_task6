from django.contrib import admin
from django.urls import path,include

from schoolapp import views
urlpatterns = [
    path("login/",views.login_student,name="login"),
    path("student/all",views.student_list,name="student-all"),
    path('logout/', views.logout_student, name='logout'),

]
