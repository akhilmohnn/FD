# Generated by Django 5.0 on 2024-01-28 05:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0008_delete_tbl_orgverification'),
        ('Guest', '0003_tbl_organization_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_medicalshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medical_name', models.CharField(max_length=50)),
                ('medical_email', models.CharField(max_length=50)),
                ('medical_contact', models.CharField(max_length=50)),
                ('medical_address', models.CharField(max_length=50)),
                ('medical_photo', models.FileField(upload_to='MedicalDoc/')),
                ('medical_proof', models.FileField(upload_to='MedicalDoc/')),
                ('medical_password', models.CharField(max_length=50)),
                ('status', models.CharField(default=0, max_length=50, null=True)),
                ('medical_place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_place')),
            ],
        ),
    ]
