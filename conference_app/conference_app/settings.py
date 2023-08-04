"""
Django settings for conference_app project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os.path
from pathlib import Path
from dotenv import load_dotenv

# from dotenv import load_dotenv

load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", "secret_key")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if os.getenv("DEBUG") == "True" else False

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "Konferencijos",
    "Renginiai",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'conference_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # BACKEND interpretuoja mūsų html failus prieš juos išsiūsdamas į naršyklę,
        'DIRS': [os.path.join(BASE_DIR, "templates"), os.path.join(BASE_DIR, "Konferencijos/Templates"), os.path.join(BASE_DIR, "Renginiai/templates")],
        # šita funkcija nurodo kelią iki bazinio templates folderio, Django jį sujungia
        # čia mes nurodom Django, kad žiūrėtų papildomai į šitą papildomą aplankalą, nes kitaip jis jo nematytų
        'APP_DIRS': True, # Automatiškai ieško template failų sukurtuose APPSUOSE
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'conference_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# LOGIN_REDIRECT_URL = '/Konferencijos/'    po logino suveikimo mus nukreis tiesiai į šitą url linką
# (galime parašyti bet kokį nukreipiamajį linką pvz pradžios linką)
LOGIN_REDIRECT_URL = '/Konferencijos/'

# MEDIA_ROOT aplankalas į kurį bus keliamos mūsų nuotraukos (aplankas - "images")
MEDIA_ROOT = os.path.join(BASE_DIR, "images")
# MEDIA_URL nurodo kaip tos nuotraukos bus pasiekiamos
MEDIA_URL = "/media/"
STATIC_ROOT = Path(BASE_DIR / 'static')



LOGGING = {
'version': 1,
'disable_existing_loggers': False,
'handlers': {
'console': {
'level': 'DEBUG',
'class': 'logging.StreamHandler',
},
'logfile': {
'level': 'DEBUG',
'class': 'logging.FileHandler',
'filename': os.path.join(BASE_DIR, 'django-logfile'),
},
},
'root': {
'level': 'INFO',
'handlers': ['console', 'logfile']
},
}