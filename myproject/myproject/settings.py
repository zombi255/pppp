# myproject/settings.py

from pathlib import Path

# بناء مسارات المشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# إعدادات الأمان
SECRET_KEY = 'django-insecure-k8zdvx-51v1gknd5-_$d98mxmipemayzx)^8t2i^dv(!u*f9&*'
DEBUG = True  # غيّر إلى False في الإنتاج
ALLOWED_HOSTS = [
    "projet-idl-cours.onrender.com",
]

# التطبيقات المثبتة
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cours',  # التطبيق الخاص بك
    'corsheaders',
]

# الـ Middleware
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

# القوالب Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # ضع مسارات قوالب إضافية إذا لزم
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'

# قاعدة البيانات
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'demodb_8fyj',
        'USER': 'demodb_8fyj_user',
        'PASSWORD': 'QgWOL4zv9iydMgSlgjl6heRkXXkhjNwc',
        'HOST': 'dpg-d4k84fruibrs73fatrsg-a.oregon-postgres.render.com',
        'PORT': '5432',
    }
}

# التحقق من كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# الإعدادات الدولية
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ملفات static
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"  # هذا المجلد الذي سينشأ عند collectstatic

# إعدادات افتراضية
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
APPEND_SLASH = True

# إعدادات CORS
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://your-frontend.com",
]
CORS_ALLOW_HEADERS = [
    "content-type",
    "authorization",
]
CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
    "OPTIONS",
]
