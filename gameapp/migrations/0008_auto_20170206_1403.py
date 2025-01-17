# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 14:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gameapp', '0007_auto_20170205_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxonomy',
            name='slug',
            field=models.SlugField(default='a'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='game',
            name='desc',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='pic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gameapp.Asset'),
        ),
        migrations.AlterField(
            model_name='user',
            name='register_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
