from django.contrib import admin
from .models import Student, Attendance, ExtraCurricular, Accounts, HostelDetails

# Customizing the Student model display
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('registration_number', 'first_name', 'last_name', 'branch', 'department', 'year', 'email')
    search_fields = ('registration_number', 'first_name', 'last_name', 'email')
    list_filter = ('branch', 'department', 'year')


# Customizing the Attendance model display
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('registration_number', 'date', 'status', 'faculty', 'subject')
    search_fields = ('registration_number__registration_number', 'faculty', 'subject')
    list_filter = ('status', 'date')


# Customizing the ExtraCurricular model display
@admin.register(ExtraCurricular)
class ExtraCurricularAdmin(admin.ModelAdmin):
    list_display = ('registration_number', 'activity_name', 'participation_date', 'achievement')
    search_fields = ('registration_number__registration_number', 'activity_name')
    list_filter = ('participation_date',)


# Customizing the Accounts model display
@admin.register(Accounts)
class AccountsAdmin(admin.ModelAdmin):
    list_display = ('registration_number', 'fee_status', 'amount_due', 'last_payment_date')
    search_fields = ('registration_number__registration_number',)
    list_filter = ('fee_status', 'last_payment_date')


# Customizing the HostelDetails model display
@admin.register(HostelDetails)
class HostelDetailsAdmin(admin.ModelAdmin):
    list_display = ('registration_number', 'hostel_name', 'room_number', 'warden_name', 'contact_number')
    search_fields = ('registration_number__registration_number', 'hostel_name', 'warden_name', 'room_number')
    list_filter = ('hostel_name', )
