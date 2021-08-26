# Generated by Django 3.2.5 on 2021-08-25 14:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='room_name',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='message',
            name='time_stamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 25, 21, 43, 54, 827569)),
        ),
    ]