from django.shortcuts import render
from .models import Student, Attendance, HostelDetails

# Home View
def home(request):
    return render(request, 'home.html')

# Student List View
def student_list(request):
    students = Student.objects.all()  # Fetch all students
    return render(request, 'students.html', {'students': students})

# Attendance List View
def attendance_list(request):
    attendance = Attendance.objects.all()
    return render(request, 'attendance.html', {'attendance': attendance})

# Hostel List View
def hostel_list(request):
    hostel_details = HostelDetails.objects.all()
    return render(request, 'hostel.html', {'hostel_details': hostel_details})
