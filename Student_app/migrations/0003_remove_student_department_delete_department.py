# Generated by Django 4.2.7 on 2023-12-05 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Student_app', '0002_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='department',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
    ]
