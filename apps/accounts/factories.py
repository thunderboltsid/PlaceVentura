# -*- coding: utf-8 -*-
import random

import factory

from apps.accounts.models import Account

__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class AccountFactory(factory.DjangoModelFactory):
    class Meta:
        model = Account
        django_get_or_create = ["email"]

    username = factory.sequence(lambda x: str(random.random()))
    password = factory.PostGenerationMethodCall('set_password',
                                                'defaultpassword')
    email = factory.sequence(lambda x: str(random.randint(1, 100)) + "a@b.de" + str(x))
    first_name="alfred"
