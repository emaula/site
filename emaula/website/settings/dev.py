"""
This is the settings file that you use when you're working on
the project locally. Local development-specific settings include
DEBUG mode, log level, and activation of developer tools like
django-debug-toolbar.
"""
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['emaula-rsip22207208.codeanyapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
