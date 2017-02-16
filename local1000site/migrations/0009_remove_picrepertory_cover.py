# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('local1000site', '0008_picrepertory_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picrepertory',
            name='cover',
        ),
    ]
