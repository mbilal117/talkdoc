# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TalkDoc', '0025_auto_20150728_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmentbooking',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
