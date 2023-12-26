from django.db import models
from django.contrib.auth.models import User 
from patient.models import Patient
# Create your models here.


class Specialization(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name
class Designation(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name

class AvailableTime(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name


class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "user")
    image = models.ImageField(upload_to="doctor/images/", null=True, blank = True)
    designation = models.ManyToManyField(Designation, related_name="designations")
    specialization = models.ManyToManyField(Specialization, related_name="specializations")
    available_time = models.ManyToManyField(AvailableTime)
    fee = models.IntegerField()
    meet_link = models.CharField(max_length=100, blank = True, null = True)
    
    def __str__(self):
    #     return 
        return f"{self.user.first_name} {self.user.last_name}"


STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]

class Review(models.Model):
    reviewer = models.ForeignKey(Patient, on_delete = models.CASCADE, null = True, blank = True)
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(choices=STAR_CHOICES, max_length = 10)
    
    def __str__(self):
        return f"Patient : {self.reviewer.user.first_name}, Doctor : {self.doctor.user.first_name}"
