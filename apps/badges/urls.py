from django.conf.urls import patterns, url
from django.contrib import admin

from apps.badges.views import BadgeDetail, BadgeList
admin.autodiscover()

urlpatterns = patterns(
    '',
    url('^/?$', BadgeList.as_view(),name='badge-list'),
    url('^(?P<pk>[-\w]+)/?$', BadgeDetail.as_view(),name='badge-detail'),
)



