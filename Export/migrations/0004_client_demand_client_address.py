# Generated by Django 3.2.3 on 2021-06-03 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Export', '0003_auto_20210603_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='client_demand',
            name='client_address',
            field=models.CharField(default='C', max_length=100),
            preserve_default=False,
        ),
    ]
