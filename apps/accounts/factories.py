# -*- coding: utf-8 -*-
import datetime
from random import randint

import factory

from apps.accounts.models import Account

__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

class AccountFactory(factory.DjangoModelFactory):
    class Meta:
        model = Account
        django_get_or_create=["email"]

    first_name = u"Łukasz"
    middle_name = u"Matteusz"
    last_name = u"Knüppel"
    second_last_name = u"Goméz"
    password = factory.PostGenerationMethodCall('set_password',
                                                'defaultpassword')
    email = factory.sequence(lambda x: str(randint(1,100)) + "a@b.de" + str(x))
    birthday = datetime.datetime.today().date()
    gender = "m"

    # Information important for events
    tshirt_size = "mxxl"
    passport_number = "asdad"
    #Information important for companies
    field_of_study = "ee"
    food_preferences = "vegan"
    # curriculum_vitae = factory.django.FileField(name="lol.txt")





