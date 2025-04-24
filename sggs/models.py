from django.db import models

class Student(models.Model):
    registration_number = models.CharField(max_length=15, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    branch = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    year = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return f"{self.registration_number} - {self.first_name} {self.last_name}"


class Attendance(models.Model):
    registration_number = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])
    faculty = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return f"Attendance for {self.registration_number} on {self.date}"


class ExtraCurricular(models.Model):
    registration_number = models.ForeignKey(Student, on_delete=models.CASCADE)
    activity_name = models.CharField(max_length=100)
    participation_date = models.DateField()
    achievement = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.activity_name} - {self.registration_number}"


class Accounts(models.Model):
    registration_number = models.ForeignKey(Student, on_delete=models.CASCADE)
    fee_status = models.CharField(max_length=10, choices=[('Paid', 'Paid'), ('Pending', 'Pending')])
    amount_due = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    last_payment_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Accounts for {self.registration_number}"


class HostelDetails(models.Model):
    registration_number = models.ForeignKey(Student, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    hostel_name = models.CharField(max_length=100)
    warden_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    
    def __str__(self):
        return f"Hostel Details for {self.registration_number} - Room {self.room_number}"
