# Generated by Django 3.2.3 on 2021-06-05 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing_details', '0002_auto_20210521_1658'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_ID', models.IntegerField()),
                ('working_hour', models.FloatField()),
                ('month', models.TextField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
