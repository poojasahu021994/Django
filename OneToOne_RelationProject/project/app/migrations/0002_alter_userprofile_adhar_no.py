# Generated by Django 5.1.5 on 2025-01-20 10:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='adhar_no',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.adhare'),
        ),
    ]
