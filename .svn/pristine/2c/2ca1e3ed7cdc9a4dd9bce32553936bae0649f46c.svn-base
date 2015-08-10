# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TalkDoc', '0005_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='services_offerd',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='services_offerd',
            field=models.ManyToManyField(to='TalkDoc.ServiceOffered'),
        ),
    ]
