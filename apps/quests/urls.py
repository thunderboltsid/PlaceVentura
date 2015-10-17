from django.conf.urls import patterns, url
from django.contrib import admin

from apps.quests.views import QuestList, QuestDetail

admin.autodiscover()
# App includes


urlpatterns = patterns(
    '',
    url('^/?$', QuestList.as_view(),name='quest-list'),
    url('^(?P<pk>[-\w]+)/?$', QuestDetail.as_view(),name='quest-detail'),
)

