# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-24 01:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pattern_generator', '0003_auto_20160523_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurements',
            name='hip',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
    ]
