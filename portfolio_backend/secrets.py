import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# Application definition
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    'SECRET_KEY', 'z2$_ua%ul(g)#arclgxub@=drl0eg+g3v!4@-!pm8da7o)-k^7')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', True)

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", 'localhost').split(" ")

# FORCE_SCRIPT_NAME = '/api'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# CORS_ORIGIN_WHITELIST = [
#     'http://localhost:3000',
#     'http://localhost:4203',
#     'http://192.168.0.105:4200',
# ]

SITE_ID = 1
