# Generated by Django 3.2.15 on 2023-01-03 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myschoolapp', '0009_communitygroup_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0)),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myschoolapp.communitygroup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointment', to='myschoolapp.teacherlogin')),
            ],
        ),
    ]
