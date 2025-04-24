from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                  # Homepage
    path('students/', views.student_list, name='students'),  # Student list
    path('attendance/', views.attendance_list, name='attendance'),  # Attendance list
    path('hostel/', views.hostel_list, name='hostel'),   # Hostel details
]
