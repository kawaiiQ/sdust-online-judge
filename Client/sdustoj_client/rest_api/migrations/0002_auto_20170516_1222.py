# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-16 12:22
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursegrouprelation',
            name='weight',
            field=models.DecimalField(decimal_places=10, default=1, max_digits=19),
        ),
        migrations.AddField(
            model_name='coursestudentrelation',
            name='score',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='coursestudentrelation',
            name='score_detail',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='missiongroup',
            name='weight',
            field=models.DecimalField(decimal_places=10, default=1, max_digits=19),
        ),
        migrations.AddField(
            model_name='missiongrouprelation',
            name='weight',
            field=models.DecimalField(decimal_places=10, default=1, max_digits=19),
        ),
        migrations.AddField(
            model_name='missionproblemrelation',
            name='weight',
            field=models.DecimalField(decimal_places=10, default=1, max_digits=19),
        ),
    ]
