# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameapp', '0014_taxonomy_games'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameplay',
            name='state',
            field=models.TextField(blank=True, null=True),
        ),
    ]
