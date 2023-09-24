# Generated by Django 4.2.2 on 2023-07-24 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0022_notificationcheftostaff_notificationcheftostudent'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationStaffToStudent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('student_id', models.IntegerField()),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]