# Generated by Django 3.1.3 on 2021-01-08 11:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='F', max_length=1)),
                ('date_of_admission', models.DateField(default=datetime.date(2021, 1, 8))),
                ('date_of_leaving', models.DateField(blank=True, null=True)),
                ('education', models.CharField(choices=[('10', '10th Pass'), ('12', '12th Pass'), ('D', 'Diploma')], max_length=30)),
                ('height', models.IntegerField(help_text='Please enter height in cms')),
            ],
        ),
        migrations.CreateModel(
            name='Marriage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ailments', models.CharField(blank=True, max_length=100)),
                ('job', models.CharField(blank=True, max_length=20)),
                ('preferences', models.TextField(default=' ')),
                ('status', models.CharField(choices=[('M', 'Married'), ('UM', 'Unmarried')], max_length=30)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preferred_location', models.TextField(default=' ')),
                ('date_of_joining', models.DateField(default=datetime.date(1000, 1, 1))),
                ('future_preferences', models.TextField()),
                ('job_timings', models.TextField()),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]