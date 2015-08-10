# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TalkDoc', '0023_employmenthistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='PracticeLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_deleted', models.DateTimeField(null=True, blank=True)),
                ('location', models.CharField(max_length=100, null=True, blank=True)),
                ('flat_plot_number', models.CharField(max_length=100, null=True, blank=True)),
                ('street_number', models.CharField(max_length=100, null=True, blank=True)),
                ('area', models.CharField(max_length=100, null=True, blank=True)),
                ('country', models.CharField(max_length=20, null=True, blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(blank=True, to='TalkDoc.City', null=True)),
                ('hospital', models.ForeignKey(to='TalkDoc.Hospital', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='hospitals',
        ),
        migrations.AddField(
            model_name='practicelocation',
            name='profile',
            field=models.ForeignKey(blank=True, to='TalkDoc.UserProfile', null=True),
        ),
    ]
