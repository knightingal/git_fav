# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('local1000site', '0003_auto_20151129_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shiprepertory',
            name='dir_name',
            field=models.CharField(max_length=256),
        ),
    ]
