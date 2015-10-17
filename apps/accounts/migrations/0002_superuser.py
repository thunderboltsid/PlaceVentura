# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import guardian.mixins
from apps.accounts.models import Account


def seed_admin(aapps,schema):
    try:
        ac=Account.objects.create_superuser("admin@eestec.net","1234")
        ac.first_name="default"
        ac.last_name="default"
        ac.gender="f"
        ac.save()
        print "Created account admin@eestec.net.net with password 1234"
    except:
        raise
class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial')
    ]

    operations = [
        migrations.RunPython(seed_admin ),
    ]
