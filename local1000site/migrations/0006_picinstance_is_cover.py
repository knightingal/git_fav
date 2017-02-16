# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('local1000site', '0005_shippic_pic_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='picinstance',
            name='is_cover',
            field=models.BooleanField(default=False),
        ),
    ]
