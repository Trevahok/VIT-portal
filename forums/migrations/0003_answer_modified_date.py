# Generated by Django 2.0.7 on 2018-10-20 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0002_auto_20181019_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
