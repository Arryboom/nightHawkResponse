# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-15 23:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nighthawk', '0002_auto_20160815_0401'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='task_urgency',
            field=models.CharField(max_length=20, null=True),
        ),
    ]