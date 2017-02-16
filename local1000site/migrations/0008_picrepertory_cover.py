# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('local1000site', '0007_auto_20160815_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='picrepertory',
            name='cover',
            field=models.CharField(default='', max_length=64),
        ),
    ]
