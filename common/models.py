from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import CharField, DateField, BooleanField, ForeignKey, TextField, \
    AutoField, SET_NULL, ImageField, PositiveIntegerField, FloatField, URLField
from polymorphic import PolymorphicModel


