# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TalkDoc', '0006_auto_20150707_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='cell_phone',
            field=models.CharField(default=b'', max_length=13),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.FileField(default=b'', max_length=200, null=True, upload_to=b'TalkDoc/Files', blank=True),
        ),
    ]
