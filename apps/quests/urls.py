from django.conf.urls import patterns, url
from django.contrib import admin

from apps.quests.views import QuestList, QuestDetail, ResponseCreate

admin.autodiscover()
# App includes


urlpatterns = patterns(
    '',
    url(r'^/?$', QuestList.as_view(),name='quest-list'),
    url(r'^response/?$', ResponseCreate.as_view(),name='response-create'),
    url(r'^(?P<pk>[-\w]+)/?$', QuestDetail.as_view(),name='quest-detail'),
)

