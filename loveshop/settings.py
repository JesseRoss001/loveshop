import os
import dj_database_url
import environ

# Initialize environment variables
env = environ.Env()
# Assuming the .env file is located at the same level as manage.py
environ.Env.read_env(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

from pathlib import Path



STRIPE_SECRET_KEY = env('STRIPE_SECRET_KEY')
STRIPE_PUBLISHABLE_KEY = env('STRIPE_PUBLISHABLE_KEY')
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-nc#^$gs3+t@+s+g1^y8p*+#6@#4y9qjxuc)%-ijb%6!b19q3g^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# Add the Gitpod and Heroku hostnames to ALLOWED_HOSTS  
ALLOWED_HOSTS = ['loveshop-037a9f640521.herokuapp.com', 'localhost', '127.0.0.1','8000-jesseross001-loveshop-l66tcfpckvd.ws-eu108.gitpod.io',]
CSRF_TRUSTED_ORIGINS = [
    'https://localhost',
    'https://127.0.0.1',
    'https://8000-jesseross001-loveshop-l66tcfpckvd.ws-eu108.gitpod.io',
    'https://loveshop-037a9f640521.herokuapp.com'
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'products',
    'loveshop',
    'accounts',
    'checkout',
    'contact',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this line for WhiteNoise
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'loveshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Add this line to include your templates directory
        'APP_DIRS': True,
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

WSGI_APPLICATION = 'loveshop.wsgi.application'

# Database configuration
DATABASES = {
    'default': dj_database_url.config(default='postgres://vqxjheds:1nrdvdG2fkWUbcvRB-bjE_xYyKiMlCh9@trumpet.db.elephantsql.com/vqxjheds')
}

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Additional locations of static files
# Comment out or remove this if you're not using local static directories
# STATICFILES_DIRS = [
#     BASE_DIR / "static",
# ]

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Cloudinary settings for static and media management
CLOUDINARY_STORAGE = {
    'CLOUDINARY_CLOUD_NAME': env('CLOUDINARY_CLOUD_NAME'),
    'CLOUDINARY_API_KEY': env('CLOUDINARY_API_KEY'),
    'CLOUDINARY_API_SECRET': env('CLOUDINARY_API_SECRET')
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'