from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name
class Specialization(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name
class Designation(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

class ScheduleTime(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name



class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "user")
    image = models.ImageField(upload_to="doctor/images/", null=True, blank = True)
    department = models.OneToOneField(Department, on_delete=models.CASCADE)
    designation = models.ManyToManyField(Designation, related_name="designations")
    specialization = models.ManyToManyField(Specialization, related_name="specializations")
    fee = models.IntegerField()
    meet_link = models.CharField(max_length=100, blank = True, null = True)
    def __str__(self):
    #     return 
        return f"{self.user.first_name} {self.user.last_name} {', '.join(str(designation) for designation in self.designation.all())}"


class AvialableTimeForDoctor(models.Model):
    doctor = models.ManyToManyField(Doctor)
    time = models.ManyToManyField(ScheduleTime)
    def __str__(self):
        doctors_str = ", ".join(f"{doctor.user.first_name} {doctor.user.last_name}" for doctor in self.doctor.all())
        times_str = ", ".join(str(time) for time in self.time.all())
        return f"Available times for {doctors_str}: {times_str}"
# class AvailableTime(models.Model):
#     name = models.CharField(max_length = 100)
#     doctor = models.ManyToManyField(Doctor)
#     # def __str__(self):
#     #     return f"Dr. {self.doctor.user.first_name} {self.doctor.user.first_name} Avialable Time : {self.name}"


