# Generated by Django 4.2.7 on 2023-12-07 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Student_app', '0008_rank'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_marks',
            old_name='subjects',
            new_name='subject',
        ),
    ]
