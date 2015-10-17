from django.db.models import Model, TextField, CharField, ManyToManyField, ForeignKey, FloatField, ImageField

__author__ = 'siddharthshukla'

class Badge(Model):
    name = CharField(max_length=64, null=True, blank=True)
    description = CharField(max_length=160, null=True, blank=True)
    thumbnail = ImageField(upload_to="users",null=True,blank=True,default="/media/cvs/example.jpg")
    user = ManyToManyField("accounts.Account",null=True,blank=True)