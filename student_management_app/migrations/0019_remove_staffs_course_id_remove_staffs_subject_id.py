# Generated by Django 4.2.2 on 2023-07-14 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0018_alter_staffs_subject_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staffs',
            name='course_id',
        ),
        migrations.RemoveField(
            model_name='staffs',
            name='subject_id',
        ),
    ]