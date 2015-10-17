# -*- coding: utf-8 -*-
import datetime
from random import randint

import factory

from apps.accounts.models import Account
from apps.quests.models import Quest

__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

class QuestFactory(factory.DjangoModelFactory):
    class Meta:
        model = Quest
    title =  factory.Sequence(lambda n: 'title '+str(n))
    description= "default_description"
    type="geo"
    precision=3.14



