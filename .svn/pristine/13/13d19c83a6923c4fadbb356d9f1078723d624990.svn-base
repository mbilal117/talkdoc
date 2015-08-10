# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TalkDoc', '0002_speciality'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceOffered',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('service_name', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('speciality', models.ForeignKey(to='TalkDoc.Speciality')),
            ],
        ),
    ]
