# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameapp', '0016_auto_20170215_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='url',
            field=models.FileField(upload_to=''),
        ),
    ]
