from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from settings.conf.media import MEDIA_ROOT

admin.autodiscover()
# App includes
# Orphans
urlpatterns = patterns(
    '',
    url(r'^quests/', include('apps.quests.urls')),
    url(r'^people/', include('apps.accounts.urls')),
)
urlpatterns += patterns(
    '',
    url('^', include('django.contrib.auth.urls')),
)
# Redirects
# If DEBUG is set, include the local file server
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += patterns(
        '',
        url(r'^__debug__/', include(debug_toolbar.urls)),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': MEDIA_ROOT}),
    )
# Third party apps and pages


from django_statsd.urls import urlpatterns as statsd_patterns

urlpatterns += patterns(
    '',
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^services/timing/', include(statsd_patterns)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='base/index.html'), name='home'),
)
