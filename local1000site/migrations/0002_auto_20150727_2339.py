# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('local1000site', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='picinstance',
            old_name='question',
            new_name='repertory',
        ),
    ]
