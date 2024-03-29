# Generated by Django 4.2.7 on 2023-12-06 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Student_app', '0006_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjects',
            name='student',
        ),
        migrations.CreateModel(
            name='Student_marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student_app.student')),
                ('subjects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student_app.subjects')),
            ],
        ),
    ]
