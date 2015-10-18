# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import apps.accounts.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='account',
            managers=[
                ('objects', apps.accounts.models.EestecerManager()),
            ],
        ),
        migrations.AlterField(
            model_name='account',
            name='gender',
            field=models.CharField(blank=True, max_length=15, null=True, choices=[(b'm', b'Male'), (b'f', b'Female'), (b'x', b'Other')]),
        ),
    ]
