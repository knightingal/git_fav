# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('local1000site', '0006_picinstance_is_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picinstance',
            name='is_cover',
            field=models.IntegerField(default=0),
        ),
    ]
