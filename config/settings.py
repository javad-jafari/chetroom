from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-g4(4vr^h3^axcb1!%@f=l@z@m=wci^k@o9o$6o6$!od8wb=s5r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    "debug_toolbar",
    'schema_graph',
    'django_extensions',
    'generic_relations',
    'django_filters',
    'new',
    'user',
    'chat.apps.ChatConfig',
    'channels',
    'rest_framework.authtoken'
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'
ASGI_APPLICATION = 'config.asgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

GRAPH_MODELS ={
    'all_applications': True,
    'graph_models': True,
     }

AUTH_USER_MODEL='user.CustomUser'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
    # 'rest_framework.authentication.SessionAuthentication',
    'rest_framework.authentication.BasicAuthentication',
]
}

"""
←[31m[auth]←[0m
    changepassword
    createsuperuser

←[31m[contenttypes]←[0m
    remove_stale_contenttypes

←[31m[debug_toolbar]←[0m
    debugsqlshell

←[31m[django]←[0m
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver

←[31m[django_extensions]←[0m
    admin_generator
    clean_pyc
    clear_cache
    compile_pyc
    create_command
    create_jobs
    create_template_tags
    delete_squashed_migrations
    describe_form
    drop_test_database
    dumpscript
    export_emails
    find_template
    generate_password
    generate_secret_key
    graph_models
    list_model_info
    list_signals
    mail_debug
    managestate
    merge_model_instances
    notes
    pipchecker
    print_settings
    print_user_for_session
    raise_test_exception
    reset_db
    reset_schema
    runjob
    runjobs
    runprofileserver
    runscript
    runserver_plus
    set_default_site
    set_fake_emails
    set_fake_passwords
    shell_plus
    show_template_tags
    show_urls
    sqlcreate
    sqldiff
    sqldsn
    sync_s3
    syncdata
    unreferenced_files
    update_permissions
    validate_templates

←[31m[rest_framework]←[0m
    generateschema

←[31m[sessions]←[0m
    clearsessions

←[31m[staticfiles]←[0m
    collectstatic
    findstatic
    runserver
"""