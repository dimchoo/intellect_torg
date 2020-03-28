import os

from intellect_torg.secret_settings import \
    PROJECT_SECRET_KEY, \
    PROJECT_DATABASE_NAME, \
    PROJECT_DATABASE_USER, \
    PROJECT_DATABASE_PASSWORD


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = PROJECT_SECRET_KEY

DEBUG = False

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'ckeditor',
    'ckeditor_uploader',
    'widget_tweaks',
    'import_export',
    'django_unused_media',
    'pytils',

    'main_app',

    'django_cleanup',
]

CKEDITOR_UPLOAD_PATH = 'ck_uploads'

IMPORT_EXPORT_USE_TRANSACTIONS = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'intellect_torg.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), BASE_DIR]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'main_app.context_processors.categories_processor',
                'main_app.context_processors.brands_processor',
                'main_app.context_processors.contact_phones_processor',
                'main_app.context_processors.subscribe_form_processor',
                'main_app.context_processors.shop_partners_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'intellect_torg.wsgi.application'


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }

DATABASES = {
    'default': {
            'NAME': PROJECT_DATABASE_NAME,
            'ENGINE': 'django.db.backends.postgresql',
            'USER': PROJECT_DATABASE_USER,
            'PASSWORD': PROJECT_DATABASE_PASSWORD,
            'HOST': '127.0.0.1'
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

try:
    from .local_settings import *
except ImportError:
    pass
