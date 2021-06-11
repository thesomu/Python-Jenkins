# Generated by Django 3.2.3 on 2021-05-23 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Export',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billing_amt', models.IntegerField()),
                ('date_of_export', models.CharField(max_length=20)),
                ('gst_imposed', models.CharField(max_length=20)),
                ('exported_to', models.CharField(max_length=20)),
                ('order_ID', models.IntegerField(max_length=20)),
                ('quantity', models.IntegerField()),
                ('estimated_time', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='imported',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billing_amt', models.IntegerField()),
                ('date_of_import', models.CharField(max_length=20)),
                ('gst_imposed', models.CharField(max_length=20)),
                ('imported_from', models.CharField(max_length=20)),
                ('order_ID', models.IntegerField(max_length=20)),
                ('quantity', models.IntegerField()),
                ('estimated_time', models.CharField(max_length=50)),
            ],
        ),
    ]
