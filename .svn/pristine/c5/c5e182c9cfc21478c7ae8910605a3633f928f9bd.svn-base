# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TalkDoc', '0017_auto_20150723_1308'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentBooking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_deleted', models.DateTimeField(null=True, blank=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('appointment_by', models.ForeignKey(related_name='Patient', to=settings.AUTH_USER_MODEL)),
                ('appointment_to', models.ForeignKey(related_name='Doctor', to='TalkDoc.UserProfile')),
                ('service_type', models.ForeignKey(to='TalkDoc.ServiceOffered')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
