# Generated by Django 3.1.3 on 2020-12-01 13:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20201201_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 1, 13, 8, 7, 720875, tzinfo=utc)),
        ),
    ]