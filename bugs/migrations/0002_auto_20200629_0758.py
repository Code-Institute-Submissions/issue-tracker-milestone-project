# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-29 07:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug',
            name='created_date',
            field=models.DateTimeField(default=datetime.date.today, null=True),
        ),
        migrations.AddField(
            model_name='bug',
            name='finished_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bug',
            name='tag',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='bug',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
