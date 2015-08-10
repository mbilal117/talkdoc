# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('TalkDoc', '0014_auto_20150723_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availability',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2015, 7, 23, 6, 19, 25, 811726, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='availability',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2015, 7, 23, 6, 19, 28, 819356, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='availability',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 7, 23, 6, 19, 33, 102221, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='availability',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2015, 7, 23, 6, 19, 35, 624726, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
