from django.contrib import admin
from . import models
# Register your models here.
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
# admin.site.register(models.Appointment)

class AppointmentAdmin(admin.ModelAdmin):
    # list_display = ('id', 'doctor', 'patient', 'appointment_status', 'appointment_type', 'time')
    # list_filter = ('doctor', 'patient', 'appointment_status', 'appointment_type')
    # search_fields = ('doctor__user__username', 'patient__user__username', 'appointment_status')

    def save_model(self, request, obj, form, change):
        # if obj.appointment_status == 'Running' and obj.appointment_type == 'Offline' and 'appointment_status' in form.changed_data:
        #     obj.send_email_to_patient()  # Assuming you have defined send_email_to_patient in the Appointment model
        obj.save()
        if obj.appointment_status == 'Running' and obj.appointment_type == 'Online':
            message = render_to_string("admin_email.html", {
                'user' : obj.patient.user,
                'doctor' : obj.doctor,
            })
            send_email = EmailMultiAlternatives("Online Appointment : Join the meet link", '', to=[obj.patient.user.email])
            send_email.attach_alternative(message, "text/html")
            send_email.send()
            

admin.site.register(models.Appointment, AppointmentAdmin)