# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TalkDoc', '0016_serviceavailability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceavailability',
            name='service',
            field=models.ForeignKey(blank=True, to='TalkDoc.ServiceOffered', null=True),
        ),
    ]
