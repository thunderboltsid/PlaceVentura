__author__ = 'siddharthshukla'
from random import randint
from apps.badges.models import Badge
import factory

class BadgeFactory(factory.DjangoModelFactory):
    class Meta:
        model = Badge
    name =  factory.Sequence(lambda n: 'title '+str(n))
    description= "default_description"

