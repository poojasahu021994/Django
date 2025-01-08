# Generated by Django 5.1.4 on 2025-01-07 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('detail', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('volume', models.IntegerField()),
                ('subscribe', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
                ('dob', models.DateField()),
                ('password', models.CharField(max_length=16)),
                ('profile_pic', models.ImageField(upload_to='')),
                ('resume', models.FileField(upload_to='')),
            ],
        ),
    ]
