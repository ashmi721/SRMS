# Generated by Django 4.2.6 on 2023-10-14 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student_classes', '0001_initial'),
        ('students', '0002_alter_student_student_dob'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisplayResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_classes.studentclass')),
                ('select_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student')),
            ],
        ),
    ]
