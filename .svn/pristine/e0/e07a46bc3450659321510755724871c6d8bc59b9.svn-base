# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TalkDoc', '0019_userprofile_profile_step'),
    ]

    operations = [
        migrations.CreateModel(
            name='AwardsRecognitions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_deleted', models.DateTimeField(null=True, blank=True)),
                ('award_recognitions', models.CharField(max_length=100, null=True, blank=True)),
                ('year_of_award', models.CharField(max_length=10, null=True, blank=True)),
                ('awarding_institute', models.CharField(max_length=100, null=True, blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='awards',
        ),
        migrations.AddField(
            model_name='awardsrecognitions',
            name='profile',
            field=models.ForeignKey(blank=True, to='TalkDoc.UserProfile', null=True),
        ),
    ]
