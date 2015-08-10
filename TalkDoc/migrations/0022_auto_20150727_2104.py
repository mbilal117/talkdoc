# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TalkDoc', '0021_membership'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_deleted', models.DateTimeField(null=True, blank=True)),
                ('degree', models.CharField(max_length=100, null=True, blank=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('institute_board', models.CharField(max_length=100, null=True, blank=True)),
                ('grade', models.CharField(max_length=20, null=True, blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='education',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='organiations_membership',
        ),
        migrations.AddField(
            model_name='education',
            name='profile',
            field=models.ForeignKey(blank=True, to='TalkDoc.UserProfile', null=True),
        ),
    ]
