from django.contrib import admin
from apps.accounts.models import Account

__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Register your models here.
admin.site.register(Account)