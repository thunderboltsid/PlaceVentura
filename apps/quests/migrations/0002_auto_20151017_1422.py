# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badges', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='lat',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='quest',
            name='lng',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='quest',
            name='precision',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='quest',
            name='type',
            field=models.CharField(default='geo', max_length=100, choices=[(b'geo', b'geo')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='response',
            name='lat',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='response',
            name='lng',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
