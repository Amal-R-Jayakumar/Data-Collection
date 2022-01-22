from django.urls import path
from .views import create_student, edit_student_data, home, individual_student, view_students

app_name = 'studentdata'
urlpatterns = [
    path('', home, name='home'),
    path('create-student/',create_student,name='create_student'),
    path('students/',view_students,name='students'),
    path('student/<int:id>/',individual_student,name='individual_students'),
    path('student/edit/<int:id>/',edit_student_data,name='edit_student'),

    ]
