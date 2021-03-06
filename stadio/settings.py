"""
Django settings for stadio project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4=ww_nw#h@!safm(x@#9b7ga&4p4pv7xg^+)s$d$%qerpxgci='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

from unipath import Path
RUTA_PROYECTO = Path(__file__).ancestor(2)

ALLOWED_HOSTS = []

TEMPLATE_DIRS = (
RUTA_PROYECTO.child('templates'),
)


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.inicio',
    'apps.partidos',
    'apps.controlzonas',
    'apps.controlpersonal',
    'apps.controlaficionados',
    'apps.taquilla',
)

from django.core.urlresolvers import reverse_lazy
LOGIN_URL = reverse_lazy('login')
LOGIN_REDIRECT_URL = reverse_lazy('login')
LOGOUT_URL= reverse_lazy('logout')

#AUTH_PROFILE_MODULE = "apps.Perfiles"


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'stadio.urls'

WSGI_APPLICATION = 'stadio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Estadio',
        'USER': 'root', 
        'PASSWORD': 'josue', 
        'HOST': 'localhost', 
        'PORT': '', 
    }
}
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-MX'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = RUTA_PROYECTO.child('media')

# Static files (CSS, JavaScript, Images)

# https://docs.djangoproject.com/en/1.7/howto/static-files/

MEDIA_URL= 'http://127.0.0.1:8000/media/'

STATIC_URL = '/static/'

#STATICFILES_DIRS = (
#    RUTA_PROYECTO.child('static')
#    )

