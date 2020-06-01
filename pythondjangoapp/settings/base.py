
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = '+)!83krz^m$i%=uo!4b7ps2s7q=2ikcm#sw!c=#6v9er#hx8or'


ALLOWED_HOSTS = ['*']


# Application definition
INSTALLED_APPS = [
                  'django.contrib.admin',
                  'django.contrib.auth',
                  'django.contrib.contenttypes',
                  'django.contrib.messages',
                  'django.contrib.staticfiles',
                  'livereload',
                  'app',
                  'bootstrap3',
                  'bootstrap4',
                  'django.contrib.sites',
                  'django.contrib.sessions'
]

SITE_ID = 1

BOOTSTRAP4 = {
    'include_jquery': True,
}

MIDDLEWARE = [
              'django.middleware.security.SecurityMiddleware',
              'whitenoise.middleware.WhiteNoiseMiddleware',
              'django.contrib.sessions.middleware.SessionMiddleware',
              'django.middleware.common.CommonMiddleware',
              'django.middleware.csrf.CsrfViewMiddleware',
              'django.contrib.auth.middleware.AuthenticationMiddleware',
              'django.contrib.messages.middleware.MessageMiddleware',
              'django.middleware.clickjacking.XFrameOptionsMiddleware',
              ]


ROOT_URLCONF = 'pythondjangoapp.urls'

TEMPLATES = [
             {
             'BACKEND': 'django.template.backends.django.DjangoTemplates',
             'DIRS': [os.path.join(BASE_DIR, 'templates')],
             'APP_DIRS': True,
             'OPTIONS': {
             'context_processors': [
                                    'django.template.context_processors.debug',
                                    'django.template.context_processors.request',
                                    'django.contrib.auth.context_processors.auth',
                                    'django.contrib.messages.context_processors.messages',
                                    "django.template.context_processors.i18n",
                                    "django.template.context_processors.media",
                                    "django.template.context_processors.static",
                                    "django.template.context_processors.tz",
                                    ],
             },
             },
             ]

WSGI_APPLICATION = 'pythondjangoapp.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ibmclouddb',
        'USER': 'admin',
        'PASSWORD': 'Anam6111994',
        'HOST': 'ae5179f1-cbc1-4d2b-90db-fb88a5facf31.b8a5e798d2d04f2e860e54e5d042c915.databases.appdomain.cloud',
        'PORT': '30391',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_URL = '/static/'
# STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = (
                    os.path.join(BASE_DIR,'app', "static"),
                    )

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'app', 'media')

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
