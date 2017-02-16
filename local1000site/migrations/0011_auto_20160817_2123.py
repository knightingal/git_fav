# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('local1000site', '0010_picrepertory_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picrepertory',
            name='cover',
            field=models.CharField(max_length=64),
        ),
    ]
