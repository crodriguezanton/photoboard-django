# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0004_auto_20161023_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='depth',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]