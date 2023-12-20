from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class Patient(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"