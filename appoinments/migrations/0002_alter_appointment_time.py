# Generated by Django 4.2.4 on 2023-12-18 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0004_avialabletimefordoctor_scheduletime_and_more'),
        ('appoinments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='doctor.avialabletimefordoctor'),
        ),
    ]
