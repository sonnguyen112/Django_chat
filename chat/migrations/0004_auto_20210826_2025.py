# Generated by Django 3.2.5 on 2021-08-26 13:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20210826_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='time_stamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 26, 20, 25, 50, 218966)),
        ),
        migrations.AlterField(
            model_name='message',
            name='value',
            field=models.CharField(max_length=1000000),
        ),
    ]
