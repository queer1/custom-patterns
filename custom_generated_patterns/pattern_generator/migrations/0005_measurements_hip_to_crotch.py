# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-24 01:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pattern_generator', '0004_measurements_hip'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurements',
            name='hip_to_crotch',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
    ]
