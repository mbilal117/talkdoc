# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('TalkDoc', '0008_auto_20150710_0203'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_deleted', models.DateTimeField(null=True, blank=True)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('day', models.CharField(max_length=10, choices=[(b'1', b'Sunday'), (b'2', b'Monday'), (b'3', b'Tuesday'), (b'4', b'Wednesday'), (b'5', b'Thursday'), (b'6', b'Friday'), (b'7', b'Saturday')])),
                ('duration', models.CharField(max_length=10, choices=[(b'1', b'15'), (b'2', b'30'), (b'3', b'45'), (b'4', b'60')])),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('location', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='userprofile',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 14, 12, 40, 20, 539969, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='date_updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 14, 12, 40, 22, 786827, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='availability',
            name='profile',
            field=models.ForeignKey(blank=True, to='TalkDoc.UserProfile', null=True),
        ),
        migrations.AddField(
            model_name='availability',
            name='service',
            field=models.ForeignKey(to='TalkDoc.ServiceOffered'),
        ),
    ]
