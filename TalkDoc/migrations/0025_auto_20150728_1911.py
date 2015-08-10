# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TalkDoc', '0024_auto_20150728_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practicelocation',
            name='hospital',
            field=models.ForeignKey(blank=True, to='TalkDoc.Hospital', null=True),
        ),
    ]
