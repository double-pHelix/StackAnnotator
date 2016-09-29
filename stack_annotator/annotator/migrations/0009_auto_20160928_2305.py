# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-28 23:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotator', '0008_remove_annotation_position'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='video_id',
            new_name='external_id',
        ),
        migrations.AlterField(
            model_name='video',
            name='start_time',
            field=models.CharField(blank=True, max_length=16),
        ),
    ]
