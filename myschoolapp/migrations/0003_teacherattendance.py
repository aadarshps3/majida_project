# Generated by Django 3.2.16 on 2022-12-27 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myschoolapp', '0002_communitygroup'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('attendance', models.BooleanField(default=True)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myschoolapp.teacherlogin')),
            ],
        ),
    ]
