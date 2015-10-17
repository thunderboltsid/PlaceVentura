# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('thumbnail', models.ImageField(default=b'/media/cvs/example.jpg', null=True, upload_to=b'users', blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('skype', models.CharField(max_length=30, null=True, verbose_name='Skype Account', blank=True)),
                ('facebookid', models.CharField(max_length=30, null=True, verbose_name='Skype Account', blank=True)),
                ('hangouts', models.CharField(max_length=30, null=True, blank=True)),
                ('mobile', models.CharField(help_text='Please provide your phone number in +XX XXX XXXXXX format', max_length=30, null=True, verbose_name='Mobile Phone Number', blank=True)),
                ('second_last_name', models.CharField(max_length=30, verbose_name='second last name', blank=True)),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('show_date_of_birth', models.BooleanField(default=True)),
                ('receive_eestec_active', models.BooleanField(default=True)),
                ('gender', models.CharField(max_length=15, choices=[(b'm', b'Male'), (b'f', b'Female'), (b'x', b'Other')])),
                ('tshirt_size', models.CharField(blank=True, max_length=15, null=True, choices=[(b'mxs', b'Male XS'), (b'ms', b'Male S'), (b'mm', b'Male M'), (b'ml', b'Male L'), (b'mxl', b'Male XL'), (b'mxxl', b'Male XXL'), (b'mxxxl', b'Male XXXL'), (b'fxs', b'Female XS'), (b'fs', b'Female S'), (b'fm', b'Female M'), (b'fl', b'Female L'), (b'fxl', b'Female XL'), (b'fxxl', b'Female XXL'), (b'fxxxl', b'Female XXXL')])),
                ('allergies', models.CharField(max_length=50, null=True, blank=True)),
                ('passport_number', models.CharField(max_length=20, null=True, blank=True)),
                ('activation_link', models.CharField(max_length=50, null=True, blank=True)),
                ('field_of_study', models.CharField(max_length=50, choices=[(b'ee', b'Electrical Engineering'), (b'it', b'Information Technology'), (b'cs', b'Computer Science'), (b'bm', b'Biomedical Engineering'), (b'tc', b'Telecommunications'), (b'pe', b'Power Engineering'), (b'se', b'Software Engineering'), (b'au', b'Automatics'), (b'ns', b'Natural Sciences'), (b'ss', b'Social Sciences'), (b'ec', b'Economy'), (b'oe', b'Other engineering subjects'), (b'oo', b'Other')])),
                ('food_preferences', models.CharField(default=b'none', max_length=15, choices=[(b'none', b'None'), (b'kosher', b'Kosher'), (b'halal', b'Halal'), (b'nopork', b'No Pork'), (b'nofish', b'Pescarian'), (b'veggie', b'Vegetarian'), (b'vegan', b'Vegan')])),
                ('curriculum_vitae', models.FileField(default=b'/media/cvs/example.dat', null=True, upload_to=b'cvs', blank=True)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
    ]
