# ruff: noqa: ERA001, E501
"""Base settings to build other settings files upon."""

from datetime import timedelta
from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
APPS_DIR = BASE_DIR / "src"
env = environ.Env()
environ.Env.read_env(str(BASE_DIR / ".env"))


CORS_ALLOW_ALL_ORIGINS = env.bool("CORS_ALLOW_ALL_ORIGINS")
CORS_ALLOWED_ORGINS = env.list("CORS_ALLOWED_ORIGINS")


# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "django_celery_beat",
    "corsheaders",
    "rest_framework",
    "django_filters",
    "drf_spectacular",
    "rest_framework_simplejwt.token_blacklist",
    "mptt",
]

LOCAL_APPS = [
    "src.user",
    "src.blog",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIDDLEWARE
# ------------------------------------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

# ADMIN
# ------------------------------------------------------------------------------
ADMIN_URL = "admin/"
ADMINS = [("""Neeket Bhandari""", "neeket@gmail.com")]
MANAGERS = [("""Bibek Joshi""", "bibekjoshi34@gmail.com")]


# TEMPLATES
# ------------------------------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(APPS_DIR / "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"


# Database
# ------------------------------------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT"),
    },
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True


# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS")
# EMAIL_USE_SSL = env.bool("EMAIL_USE_SSL")
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL")
SERVER_EMAIL = env("SERVER_EMAIL")
EMAIL_TIMEOUT = 5


# PASSWORDS
# ------------------------------------------------------------------------------
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# FIXTURES
# ------------------------------------------------------------------------------
FIXTURE_DIRS = (str(APPS_DIR / "fixtures"),)


# SECURITY
# ------------------------------------------------------------------------------
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = "DENY"
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")


# AUTHENTICATION
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

AUTH_USER_MODEL = "user.User"

# Internationalization
# ------------------------------------------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
SITE_ID = 1
USE_I18N = True
USE_TZ = True


# STATIC
# ------------------------------------------------------------------------------
STATIC_ROOT = str(BASE_DIR / "staticfiles")
STATIC_URL = "/static/"
STATICFILES_DIRS = [str(APPS_DIR / "static")]
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# MEDIA
# ------------------------------------------------------------------------------
MEDIA_ROOT = str(APPS_DIR / "media")
MEDIA_URL = "/media/"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# LOGGING
# ------------------------------------------------------------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}


# django-rest-framework
# -------------------------------------------------------------------------------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_RENDERER_CLASSES": (
        "djangorestframework_camel_case.render.CamelCaseJSONRenderer",
        "djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer",
    ),
    "DEFAULT_PARSER_CLASSES": [
        "src.libs.parser.CustomNestedParser",
        "djangorestframework_camel_case.parser.CamelCaseFormParser",
        "djangorestframework_camel_case.parser.CamelCaseJSONParser",
    ],
    "JSON_UNDERSCOREIZE": {
        "no_underscore_before_number": True,
    },
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "EXCEPTION_HANDLER": "src.libs.exception_handler.custom_exception_handler",
    'DEFAULT_THROTTLE_RATES': {
        'anon': '5/minute',
    }
}

NESTED_FORM_PARSER = {"OPTIONS": {"allow_empty": True, "allow_blank": True}}
APPEND_SLASH = False
CORS_URLS_REGEX = r"^/api/.*$"

SPECTACULAR_SETTINGS = {
    "SCHEMA_COMPONENT_SPLIT_UNDERSCORES": False,
    "TITLE": "Blog API",
    "DESCRIPTION": "Documentation of API endpoints of Blog App",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "POSTPROCESSING_HOOKS": [
        "drf_spectacular.hooks.postprocess_schema_enums",
        "drf_spectacular.contrib.djangorestframework_camel_case.camelize_serializer_fields",
    ],
    "SERVE_PERMISSIONS": ["rest_framework.permissions.IsAuthenticated"],
    "SCHEMA_PATH_PREFIX": "/api/v1/admin",
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKEN": False,
    "BLACKLIST_AFTER_ROTATION": False,
}

# Constants
# -------------------------------------------------------------------------------
MAX_UPLOAD_SIZE = 2097152
BLOG_MEDIA_MAX_UPLOAD_SIZE = 2097152
FRONTEND_BASE_URL = env("FRONTEND_BASE_URL")
AUTH_LINK_EXP_TIME = 10


# Celery
# ------------------------------------------------------------------------------
REDIS_HOST = env("REDIS_HOST")
REDIS_PORT = env("REDIS_PORT")
REDIS_DB = env("REDIS_DB")

if USE_TZ:
    CELERY_TIMEZONE = TIME_ZONE
CELERY_BROKER_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_RESULT_EXTENDED = True
CELERY_RESULT_BACKEND_ALWAYS_RETRY = True
CELERY_RESULT_BACKEND_MAX_RETRIES = 10
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_TIME_LIMIT = 5 * 60
CELERY_TASK_SOFT_TIME_LIMIT = 60
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
CELERY_WORKER_SEND_TASK_EVENTS = True
CELERY_TASK_SEND_SENT_EVENT = True


# OAUTH
# ------------------------------------------------------------------------------
OAUTH_PROVIDERS = {
    "google": {
        "client_id": "197523093421-7dd93s0jup4ulbfovkn2krvvun0k7lph.apps.googleusercontent.com",
        "client_secret": "your-google-client-secret",
    },
    "facebook": {
        "client_id": "your-facebook-client-id",
        "client_secret": "your-facebook-client-secret",
    },
    "apple": {
        "client_id": "your-apple-client-id",
        "client_secret": "your-apple-client-secret",
    },
}
SOCIAL_SECRET = "test@9085jfJdh"

CELERY_TASK_EAGER_PROPAGATES = True

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [(REDIS_HOST, REDIS_PORT)],
        },
    },
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    },
}
