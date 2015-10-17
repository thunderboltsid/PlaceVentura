from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView, TemplateView
from apps import quests
from apps.quests.views import QuestList

from settings.conf.media import MEDIA_ROOT

admin.autodiscover()
# App includes
urlpatterns = patterns(
    '',
    url('^/?$', QuestList.as_view(),name='quest-list'),
)

