# -*- coding: utf-8 -*-
import factory

from apps.events.factories import BaseEventFactory
from common.models import Confirmable, Notification, Confirmation, Applicable, Image, \
    Report, Location


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)



