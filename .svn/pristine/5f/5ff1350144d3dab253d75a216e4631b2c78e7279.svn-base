# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TalkDoc', '0004_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_deleted', models.DateTimeField(null=True, blank=True)),
                ('dob', models.DateTimeField(null=True, blank=True)),
                ('sex', models.CharField(max_length=10, choices=[(b'Male', b'Male'), (b'Female', b'Female')])),
                ('medical_condition', models.CharField(max_length=100, null=True, blank=True)),
                ('alergy', models.CharField(max_length=50, null=True, blank=True)),
                ('picture', models.FileField(default=b'', max_length=200, null=True, upload_to=b'User/picture', blank=True)),
                ('blood_group', models.CharField(max_length=10, choices=[(b'A+', b'A+'), (b'A-', b'A-'), (b'B+', b'B+'), (b'B-', b'B-'), (b'O+', b'O+'), (b'O-', b'O-'), (b'AB+', b'AB+'), (b'AB-', b'AB-')])),
                ('marital_status', models.CharField(max_length=10, choices=[(b'Single', b'Single'), (b'Married', b'Married')])),
                ('address', models.CharField(max_length=100, null=True, blank=True)),
                ('education', models.CharField(max_length=50, null=True, blank=True)),
                ('city', models.ForeignKey(to='TalkDoc.City')),
                ('services_offerd', models.ForeignKey(to='TalkDoc.ServiceOffered')),
                ('speciality', models.ForeignKey(to='TalkDoc.Speciality')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
