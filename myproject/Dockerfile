# myproject/Dockerfile

# استخدم صورة Python رسمية
FROM python:3.11-slim-bullseye

# منع Python من إنشاء ملفات pyc وتشغيله بدون buffering
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# إنشاء مجلد العمل
WORKDIR /app

# تثبيت الحزم الأساسية للنظام
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
        gettext \
        curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# إنشاء مستخدم غير جذر
RUN useradd --create-home appuser

# نسخ ملف المتطلبات من نفس المجلد الذي فيه Dockerfile
COPY myproject/ ./


# تثبيت مكتبات Python
RUN python -m pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# نسخ باقي ملفات المشروع
COPY . .

# جمع ملفات static
RUN python manage.py collectstatic --noinput --settings=myproject.settings || true

# ضبط صلاحيات المستخدم
RUN chown -R appuser:appuser /app
USER appuser

# فتح البورت للتطبيق
EXPOSE 8000

# الأمر الافتراضي لتشغيل التطبيق
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "myproject.wsgi:application"]
