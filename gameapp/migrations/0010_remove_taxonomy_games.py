# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 23:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gameapp', '0009_taxonomy_games'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taxonomy',
            name='games',
        ),
    ]
