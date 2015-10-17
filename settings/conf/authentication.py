import datetime

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # default
    'guardian.backends.ObjectPermissionBackend',
    'social_auth.backends.facebook.FacebookBackend',
)
GUARDIAN_MONKEY_PATCH = False
ANONYMOUS_USER_ID = -1
REGISTRATION_API_ACTIVATION_SUCCESS_URL = '/'
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=30),

    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=100),

}
