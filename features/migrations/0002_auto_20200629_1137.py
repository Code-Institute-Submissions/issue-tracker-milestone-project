# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-29 11:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='features',
            name='created_date',
            field=models.DateTimeField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='features',
            name='finished_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='features',
            name='tag',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]