# Generated by Django 3.2.3 on 2021-06-08 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0002_auto_20210608_0635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empattendance',
            name='dayEight',
        ),
        migrations.RemoveField(
            model_name='empattendance',
            name='dayNine',
        ),
        migrations.RemoveField(
            model_name='empattendance',
            name='daySeven',
        ),
        migrations.RemoveField(
            model_name='empattendance',
            name='dayTen',
        ),
    ]
