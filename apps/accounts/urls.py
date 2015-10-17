from django.conf.urls import patterns, url
from django.contrib import admin

from apps.accounts.views import AccountList, AccountDetail

admin.autodiscover()
# App includes


urlpatterns = patterns(
    '',
    url('^/?$', AccountList.as_view(),name='account-list'),
    url('^/(?P<pk>[-\w]+)/?$', AccountDetail.as_view(),name='account-detail'),
)

