# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TalkDoc', '0015_auto_20150723_1119'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceAvailability',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_deleted', models.DateTimeField(null=True, blank=True)),
                ('duration', models.CharField(max_length=10, choices=[(b'1', b'15'), (b'2', b'30'), (b'3', b'45'), (b'4', b'60')])),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(blank=True, to='TalkDoc.UserProfile', null=True)),
                ('service', models.ForeignKey(to='TalkDoc.ServiceOffered')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
