# myproject/Dockerfile

# استخدم Python 3.11 slim كصورة أساسية
FROM python:3.11-slim-bullseye

# منع Python من إنشاء ملفات pyc وتشغيله بدون buffering
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# مجلد العمل داخل الحاوية
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

# إنشاء مستخدم غير جذر لتشغيل التطبيق
RUN useradd --create-home appuser

# نسخ ملف المتطلبات وتثبيته
COPY requirements.txt ./
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# نسخ باقي المشروع
COPY . .

# جمع ملفات static (يمكن تعديل settings حسب الحاجة)
RUN python manage.py collectstatic --noinput --settings=myproject.settings || true

# تعيين الصلاحيات للمستخدم العادي
RUN chown -R appuser:appuser /app
USER appuser

# فتح البورت للتطبيق
EXPOSE 8000

# الأمر الافتراضي لتشغيل التطبيق باستخدام Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "myproject.wsgi:application"]
