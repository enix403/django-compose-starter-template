from app.utils import resolve_root

from app.bootstrap.settings.components.base import (
    STATICFILES_DIRS,
    REST_FRAMEWORK
)

DEBUG = False
HTML_MINIFY = True
CSRF_FAILURE_VIEW = 'app.bootstrap.rooturls.handler_csrf_failure'


REST_FRAMEWORK = {
    **REST_FRAMEWORK,
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer'
    ]
}