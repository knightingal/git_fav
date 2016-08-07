# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('local1000site', '0004_auto_20151130_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippic',
            name='pic_type',
            field=models.CharField(max_length=8, blank=True),
        ),
    ]
