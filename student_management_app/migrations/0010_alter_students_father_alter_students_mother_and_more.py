# Generated by Django 4.2.2 on 2023-07-03 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0009_alter_students_father_alter_students_mother_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='father',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='mother',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='phone',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
