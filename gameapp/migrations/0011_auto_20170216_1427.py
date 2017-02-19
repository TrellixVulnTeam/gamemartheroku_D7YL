# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameapp', '0010_remove_taxonomy_games'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game_taxonomy',
            name='game',
        ),
        migrations.RemoveField(
            model_name='game_taxonomy',
            name='taxonomy',
        ),
        migrations.AddField(
            model_name='game',
            name='taxonomies',
            field=models.ManyToManyField(to='gameapp.Taxonomy'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='status',
            field=models.CharField(default='error', max_length=50),
        ),
        migrations.AlterField(
            model_name='asset',
            name='url',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='gameplay',
            name='score',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='gameplay',
            name='state',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Game_Taxonomy',
        ),
    ]
