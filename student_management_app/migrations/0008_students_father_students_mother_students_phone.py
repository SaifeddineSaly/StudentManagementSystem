# Generated by Django 4.2.2 on 2023-07-03 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0007_staffs_hiring_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='father',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='mother',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='phone',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
