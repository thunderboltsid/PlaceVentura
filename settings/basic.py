
import random

SILENCED_SYSTEM_CHECKS = [u"models.E005"]
from settings.conf.debugtoolbar import *
from settings.conf.templates import TEMPLATE_DIRS

try:
    from secret import FACEBOOK_APP_ID ,FACEBOOK_API_SECRET
except:
    FACEBOOK_API_SECRET="lol"
    FACEBOOK_APP_ID="thisisnotit"
WSGI_APPLICATION = 'common.wsgi.application'
AUTH_USER_MODEL = 'accounts.Account'
SOCIAL_AUTH_USER_MODEL = AUTH_USER_MODEL
FACEBOOK_EXTENDED_PERMISSIONS = ['email','public_profile']
SOCIAL_AUTH_DEFAULT_USERNAME = lambda: str(random.random())
SESSION_SERIALIZER='django.contrib.sessions.serializers.PickleSerializer'
ROOT_URLCONF = 'common.urls'
VERSION = 1

SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    'social_auth.backends.pipeline.associate.associate_by_email',
    'social_auth.backends.pipeline.user.get_username',
    'social_auth.backends.pipeline.user.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.social.load_extra_data',
    'social_auth.backends.pipeline.user.update_user_details'
)
SOCIAL_AUTH_PIPELINE += (
    'apps.accounts.views.update_avatar',
)
from conf.apps import *
# Third party apps
INSTALLED_APPS += (
    'apps.accounts',
    'apps.quests',
    'apps.badges',
    'common',
)
INSTALLED_APPS += (
    'compressor',
    'social_auth',
    # 'haystack',
    'kombu.transport.django',
    'djcelery',
    'gunicorn',
    'sorl.thumbnail',
    'corsheaders',
    'rest_framework',
    'debug_toolbar',
    # 'django_statsd',
)
INSTALLED_APPS += ("djcelery_email",)
# Own apps
from conf.static import *

LOGIN_URL = '/login-form/'
LOGIN_REDIRECT_URL = '/quests/'
LOGIN_ERROR_URL = '/login-error/'
STATICFILES_FINDERS += (
    'compressor.finders.CompressorFinder',
)

from conf.media import *
from conf.middleware import *
from conf.haystack import *
from conf.email import *
from conf.froala import *
from conf.compressor import *
from conf.localization import *
from conf.logging import *
from conf.mailqueue import *
from conf.rest import *
from conf.cors import *
from conf.authentication import *
from conf.statsd import *

AUTHENTICATION_BACKENDS

CORS_ORIGIN_WHITELIST
REST_FRAMEWORK
HAYSTACK_CONNECTIONS
COMPRESS_ENABLED
DEFAULT_FROM_EMAIL
FROALA_INCLUDE_JQUERY
TIME_ZONE
LOGGING
MAILQUEUE_CELERY
MEDIA_ROOT
MIDDLEWARE_CLASSES
TEMPLATE_DIRS
STATSD_MODEL_SIGNALS
DEBUG_TOOLBAR_PANELS
