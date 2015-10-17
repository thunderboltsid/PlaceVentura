from django.db.models import Model, TextField, CharField, ManyToManyField, ForeignKey, FloatField

__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
class Response(Model):
    user = ForeignKey('accounts.Account')
    quest = ForeignKey('quests.Quest')
    lat = FloatField(blank=True,null=True)
    lng = FloatField(blank=True,null=True)


QUEST_TYPES=[("geo","geo"),]


class Quest(Model):
    title = CharField(max_length=200,null=True,blank=True)
    description = TextField(null=True,blank=True)
    users= ManyToManyField('accounts.Account',null=True,blank=True,through='quests.Response')
    type = CharField(max_length=100,choices=QUEST_TYPES)
    lat = FloatField(blank=True,null=True)
    lng = FloatField(blank=True,null=True)
    precision = FloatField(blank=True,null=True) #TODO: Insert a default here.

