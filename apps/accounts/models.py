from django.contrib import auth
from django.contrib.auth.models import User, AbstractBaseUser, AbstractUser, \
    PermissionsMixin, Permission, _user_get_all_permissions, _user_has_perm, \
    _user_has_module_perms, GroupManager, BaseUserManager
from django.contrib.contenttypes.fields import GenericRelation
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.db.models import EmailField, CharField, BooleanField, ManyToManyField, \
    ForeignKey, DateField, FileField, IntegerField
from django.utils.translation import ugettext_lazy as _
from guardian.mixins import GuardianUserMixin
from guardian.shortcuts import assign_perm
from polymorphic import PolymorphicModel

from apps.accounts.help_texts import GROUPS_HELP_TEXT
from apps.accounts.help_texts import IS_SUPERUSER_HELP_TEXT
from settings.conf.choices import GENDER_CHOICES, TSHIRT_SIZE, FIELDS_OF_STUDY, \
    FOOD_CHOICES

__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

objects = GroupManager()



from django.db import models
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager)



class EestecerManager(BaseUserManager):
    """ A manager taking care of creating :class:`Eestecer` objects. """

    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)


FIELDS_OF_STUDY = (
    ("ee", "Electrical Engineering"),
    ("it", "Information Technology"),
    ("cs", "Computer Science"),
    ("bm", "Biomedical Engineering"),
    ("tc", "Telecommunications"),
    ("pe", "Power Engineering"),
    ("se", "Software Engineering"),
    ("au", "Automatics"),
    ("ns", "Natural Sciences"),
    ("ss", "Social Sciences"),
    ("ec", "Economy"),
    ("oe", "Other engineering subjects"),
    ("oo", "Other"),
)
FOOD_CHOICES = (
    ('none', 'None'),
    ('kosher', 'Kosher'),
    ('halal', 'Halal'),
    ('nopork', 'No Pork'),
    ('nofish', 'Pescarian'),
    ('veggie', 'Vegetarian'),
    ('vegan', 'Vegan'),
)
GENDER_CHOICES = (('m', 'Male'), ('f', 'Female'), ('x', 'Other'), )
TSHIRT_SIZE = (('mxs', 'Male XS'), ('ms', 'Male S'), ('mm', 'Male M'), ('ml', 'Male L'),
               ('mxl', 'Male XL'), ('mxxl', 'Male XXL'), ('mxxxl', 'Male XXXL'),
               ('fxs', 'Female XS'), ('fs', 'Female S'), ('fm', 'Female M'),
               ('fl', 'Female L'), ('fxl', 'Female XL'), ('fxxl', 'Female XXL'),
               ('fxxxl', 'Female XXXL'), )



class Account(AbstractBaseUser, PermissionsMixin):
    #Basic Information
    def name(self):
        return self.get_full_name()
    thumbnail = models.ImageField(upload_to="users",null=True,blank=True,default="/media/cvs/example.jpg")
    description = models.TextField(blank=True, null=True)
    #Contact information
    email = models.EmailField(_('email address'), max_length=254, unique=True)
    skype = models.CharField(_('Skype Account'), max_length=30, null=True, blank=True)
    facebookid = models.CharField(_('Skype Account'), max_length=30, null=True, blank=True)
    hangouts = models.CharField (max_length=30, null=True, blank=True)
    mobile = models.CharField(_('Mobile Phone Number'), max_length=30, null=True,
                              blank=True,
                              help_text=_(
                                  'Please provide your phone number in +XX XXX XXXXXX '
                                  'format'))
    #Names
    username   = CharField(max_length=200,blank=True,null=True)
    first_name = models.CharField(_('first name'), max_length=30)
    middle_name = models.CharField(_('middle name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30)
    second_last_name = models.CharField(_('second last name'), max_length=30, blank=True)
    """ For our friends from the iberic peninsula"""
    date_of_birth = models.DateField(blank=True, null=True)
    show_date_of_birth = models.BooleanField(default=True)
    receive_eestec_active = models.BooleanField(default=True)
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    tshirt_size = models.CharField(max_length=15, choices=TSHIRT_SIZE, blank=True,
                                   null=True)
    allergies = models.CharField(max_length=50, blank=True, null=True)
    passport_number = models.CharField(max_length=20, blank=True, null=True)
    activation_link = models.CharField(max_length=50, blank=True, null=True)
    """Passport number required by many hostels. Makes it easier for organizers."""
    field_of_study = models.CharField(max_length=50, choices=FIELDS_OF_STUDY)
    food_preferences = models.CharField(max_length=15, choices=FOOD_CHOICES,
                                        default='none')
    """ Food preferences, for example vegetarian or no pork. """
    curriculum_vitae = models.FileField(upload_to="cvs", blank=True, null=True,default="/media/cvs/example.dat")
    """ For the future incorporation of Lykeion """
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    """Should be set by the user to the time they joined eestec. For new users it will
    be the moment they register with the website"""


    #Django information
    is_staff = models.BooleanField(_('active'), default=False)
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_(
                                        'Designates whether this user should be '
                                        'treated as '
                                        'active. Unselect this instead of deleting '
                                        'accounts.'))
    """Designates whether this user should be treated as active. Unselect this instead
    of deleting accounts"""


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'gender']

    objects = EestecerManager()



    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
    def get_full_name(self):
        """ Returns the first_name plus the last_name, with a space in between. """
        full_name = self.first_name.capitalize()
        full_name+=" "+self.last_name.capitalize()
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return '%s %s' % (self.first_name, self.last_name)
    def __unicode__(self):
        return self.get_full_name()


# class Achievement(models.Model):
#     class Meta:
#         permissions = (('view_achievement', 'Can view achievement'),)
#     person = models.ForeignKey(Eestecer, related_name='achievements')
#     position = models.ForeignKey(Position)
#     member = models.ForeignKey('teams.Team', blank=True, null=True)
#     date = models.DateField(auto_now_add=True)
#     event = models.ForeignKey('events.Event', null=True, blank=True)
#     def __unicode__(self):
#         return self.person.get_short_name() + " - " + self.position.name
