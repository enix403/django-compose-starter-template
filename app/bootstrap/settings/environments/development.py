import os
from app.utils import resolve_root

from app.bootstrap.settings.components.base import (
    INSTALLED_APPS,
    STATICFILES_DIRS,
    REST_FRAMEWORK
)
from app.bootstrap.settings.components.middleware import (
    MIDDLEWARE
)


DEBUG = True

INSTALLED_APPS.extend([
    "corsheaders",
    'debug_toolbar',
    'django_extensions',
])

MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')
MIDDLEWARE.extend([
    'debug_toolbar.middleware.DebugToolbarMiddleware',
])

TEMPLATE_DEBUG = True

SHELL_PLUS = "plain"
HTML_MINIFY = True
X_ENABLE_DEBUGBAR = True

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda _: X_ENABLE_DEBUGBAR,
}

# ========================================== Third Party ==========================================

REST_FRAMEWORK = {
    **REST_FRAMEWORK,
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ]
}

CORS_PREFLIGHT_MAX_AGE = 0
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGIN_REGEXES = [
    # allow CORS on all ports of localhost (including no port)
    r"^http:\/\/localhost(:[0-9]+)?$",
    # allow CORS on all ip addrs of form 127.x.y.z[:port]
    r"^http:\/\/127\.[0-9]+\.[0-9]+\.[0-9]+(:[0-9]+)?$" 
]

