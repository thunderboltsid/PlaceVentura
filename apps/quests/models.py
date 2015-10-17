from django.db.models import Model, TextField, CharField, ManyToManyField, ForeignKey, FloatField

__author__ = 'Sebastian Wozny'
import logging
import math

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


def in_range(position, answer, accuracy):
    #radius in km
    R = 6371
    dlat = to_rad(position[0] - answer[0])
    dlon = to_rad(position[1] - answer[1])

    a = math.sin(dlat/2)**2 + math.cos(to_rad(position[0])) * \
        math.cos(to_rad(answer[0])) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a),math.sqrt(1-a))
    d = R*c

    #distance in meters
    d *= 1000
    if d<=accuracy:
        return True
    return False

def to_rad(val):
    return val * math.pi / 180
