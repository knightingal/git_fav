# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PicInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pic_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='PicRepertory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rep_name', models.CharField(max_length=256)),
                ('pub_date', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='picinstance',
            name='question',
            field=models.ForeignKey(to='local1000site.PicRepertory'),
        ),
    ]
