# Generated by Django 4.2.4 on 2023-12-18 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0004_avialabletimefordoctor_scheduletime_and_more'),
        ('appoinments', '0002_alter_appointment_time'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AvailableTime',
        ),
        migrations.AddField(
            model_name='avialabletimefordoctor',
            name='doctor',
            field=models.ManyToManyField(to='doctor.doctor'),
        ),
        migrations.AddField(
            model_name='avialabletimefordoctor',
            name='time',
            field=models.ManyToManyField(to='doctor.scheduletime'),
        ),
    ]