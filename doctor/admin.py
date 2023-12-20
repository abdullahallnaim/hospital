from django.contrib import admin
from django import forms


# class DoctorAdminForm(forms.ModelForm):
#     class Meta:
#         model = Doctor
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super(DoctorAdminForm, self).__init__(*args, **kwargs)
#         if self.instance:
#             # Limit the available_times queryset to only those associated with the current doctor instance
#             self.fields['available_times'].queryset = AvailableTime.objects.filter(doctor=self.instance)

# class DoctorAdmin(admin.ModelAdmin):
#     form = DoctorAdminForm
    # Other configurations for DoctorAdmin

# Register the Doctor model with the custom DoctorAdmin
# admin.site.register(Doctor, DoctorAdmin)
from . import models
# Register your models here.
admin.site.register(models.Doctor)
admin.site.register(models.Department)
admin.site.register(models.Designation)
admin.site.register(models.ScheduleTime)
admin.site.register(models.Specialization)