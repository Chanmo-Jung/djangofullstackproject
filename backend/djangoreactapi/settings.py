"""
Django settings for djangoreactapi project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings
and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
from datetime import timedelta
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6yfj0##&1+g_73bx(f=#vb0ld+jk!tux$%ign127*=ot5g8yl!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
APPEND_SLASH = False
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin', # 관리용 사이트
    'django.contrib.auth', # 인증시스템
    'django.contrib.contenttypes', # 컨텐츠 타입을 위한 프레임 워크
    'django.contrib.sessions', # 세션 프레임워크
    'django.contrib.messages', # 메세징 프레임워크
    'django.contrib.staticfiles', # 정적파일을 관리하는 프레임워크
    # 'userInfo.apps.userInfoConfig', # 앱 추가
    'rest_framework',
    'corsheaders', #script로 짜여진 코드에서의 다른 도메인에 대한 요청을 할 수 있게해줌

]

REST_FRAMEWORK = {
    'DEFAULT_PERMOSSION_CLASSES': (
      'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}

import datetime

JWT_AUTH = {
    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_ALGORITHM': 'HS256',
    'JWT_VERIFY_EXPIRATION': True,  # 토큰검증
    'JWT_ALLOW_REFRESH': True,  # 유효기간이 지나면 새로운 토큰반환의 refresh
    'JWT_EXPIRATION_DELTA': datetime.timedelta(minutes=60),  # Access Token의 만료 시간
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=3),  # Refresh Token의 만료 시간
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'djangoreactapi.utils.my_jwt_response_handler'
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',     # 추가
    'django.middleware.common.CommonMiddleware', # 추가
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = False
CORS_EXPOSE_HEADERS = (
    'Access-Control-Allow-Origin: http://127.0.0.1:3003',
)

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = (
    'http://127.0.0.1:3000',
    'http://localhost:3001',
    'http://localhost:3003',
    'http://127.0.0.1:3003',
    'http://127.0.0.1:3002',
    'http://39.118.174.168:8000',)

ROOT_URLCONF = 'djangoreactapi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'djangoreactapi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ecenter',
        'USER': 'ecenter',
        'PASSWORD': 'qwer1234',
        'HOST': '39.118.174.168',
        'PORT': '3307'
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
import os
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


