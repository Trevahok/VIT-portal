# Generated by Django 2.0.7 on 2018-07-11 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20180709_1654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='reg_date',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_activity_ip',
            field=models.GenericIPAddressField(default='0.0.0.0'),
        ),
    ]
