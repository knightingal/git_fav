# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('local1000site', '0002_auto_20150727_2339'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShipPic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pic_name', models.CharField(max_length=128)),
                ('pic_url', models.CharField(max_length=1024)),
                ('pic_description', models.CharField(max_length=8192)),
                ('pic_copyright', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='ShipRepertory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ship_name', models.CharField(max_length=256)),
                ('dir_name', models.CharField(max_length=16)),
            ],
        ),
        migrations.AddField(
            model_name='shippic',
            name='ship',
            field=models.ForeignKey(to='local1000site.ShipRepertory'),
        ),
    ]
