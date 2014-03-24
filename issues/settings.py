"""
Django settings for issues project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# WHO'S USING???
JAN_USING = False

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c(#5sk^j26gs9rne%c%xn4-k!8-*q=@=_8ck_l1hwlz$y0s71_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'issues.urls'

WSGI_APPLICATION = 'issues.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
if JAN_USING:
    STATIC_ROOT = '/home/janmw/djcode/issues/static'
else:
    STATIC_ROOT = '/Users/pingihu/Issues/Issues/static'

# Additional locations of static files
if JAN_USING:
    STATICFILES_DIRS = ('/home/janmw/djcode/issues/static/js',
                        '/home/janmw/djcode/issues/static/css',)
else:
    STATICFILES_DIRS = (
        '/Users/pingihu/Issues/Issues/static/js',
        '/Users/pingihu/Issues/Issues/static/css'
        # Put strings here, like "/home/html/static" or "C:/www/django/static".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.
    )


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = ( 'django.template.loaders.filesystem.Loader',
                      'django.template.loaders.app_directories.Loader',
                      # 'django.template.loaders.eggs.Loader', )
                      )

#Locations of templates
if JAN_USING:
    TEMPLATE_DIRS = ( # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates". # Always use forward slashes, even on Windows. # Don't forget to use absolute paths, not relative paths. 
    "/home/janmw/djcode/issues/templates", )
else:
    TEMPLATE_DIRS = (
    "/Users/pingihu/Issues/Issues/templates", )
