# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TalkDoc', '0013_auto_20150717_1556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='availability',
            name='day',
        ),
        migrations.RemoveField(
            model_name='availability',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='availability',
            name='service',
        ),
        migrations.AddField(
            model_name='availability',
            name='end_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='availability',
            name='is_saturday_off',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='availability',
            name='is_sunday_off',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='availability',
            name='start_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='availability',
            name='end_time',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='availability',
            name='start_time',
            field=models.TimeField(null=True, blank=True),
        ),
    ]
