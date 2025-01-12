# Generated by Django 5.1.4 on 2025-01-12 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='number_of_departments',
        ),
        migrations.RemoveField(
            model_name='company',
            name='number_of_employees',
        ),
        migrations.RemoveField(
            model_name='company',
            name='number_of_projects',
        ),
        migrations.RemoveField(
            model_name='department',
            name='number_of_employees',
        ),
        migrations.RemoveField(
            model_name='department',
            name='number_of_projects',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='days_employed',
        ),
        migrations.AlterField(
            model_name='project',
            name='assigned_employees',
            field=models.ManyToManyField(related_name='projects', to='company.employee'),
        ),
    ]
