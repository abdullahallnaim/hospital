from django.db import models
from django.contrib.auth.models import User 
from patient.models import Patient
from django.core.mail import send_mail
from doctor.models import Doctor,AvialableTimeForDoctor
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    APPOINTMENT_STATUS = (
        ('Completed', 'Completed'),
        ('Pending', 'Pending'),
        ('Running', 'Running'),
    )
    APPOINTMENT_TYPES = (
        ('Offline', 'Offline'),
        ('Online', 'Online'),
    )
    appointment_type = models.CharField(max_length=30, choices=APPOINTMENT_TYPES)
    appointment_status = models.CharField(max_length=30, choices=APPOINTMENT_STATUS)
    symtom = models.TextField()
    time = models.ForeignKey(AvialableTimeForDoctor, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Doctor Dr.{self.doctor.user.username} Patient : {self.patient.user.username}"
    