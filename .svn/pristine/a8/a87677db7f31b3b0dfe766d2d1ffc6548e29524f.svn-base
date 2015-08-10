# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TalkDoc', '0010_hospital'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='awards',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='hospitals',
            field=models.ManyToManyField(to='TalkDoc.Hospital', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='organiations_membership',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
