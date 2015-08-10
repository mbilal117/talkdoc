# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('TalkDoc', '0007_auto_20150709_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='services_offerd',
            field=models.ManyToManyField(to='TalkDoc.ServiceOffered', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='speciality',
            field=models.ForeignKey(blank=True, to='TalkDoc.Speciality', null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
