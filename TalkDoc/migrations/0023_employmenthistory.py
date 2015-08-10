# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TalkDoc', '0022_auto_20150727_2104'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmploymentHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_deleted', models.DateTimeField(null=True, blank=True)),
                ('designation', models.CharField(max_length=100, null=True, blank=True)),
                ('employer_name', models.CharField(max_length=100, null=True, blank=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('country', models.CharField(max_length=20, null=True, blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(blank=True, to='TalkDoc.City', null=True)),
                ('profile', models.ForeignKey(blank=True, to='TalkDoc.UserProfile', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
