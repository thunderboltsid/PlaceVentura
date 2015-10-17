from apps.quests.models import Quest

__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

from django.contrib import admin
# Register your models here.
admin.site.register(Quest)
