# استخدم Python 3.12 slim
FROM python:3.12-slim

# مجلد العمل داخل الحاوية
WORKDIR /app

# متغيرات التشغيل
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# تثبيت الحزم الأساسية
RUN apt-get update \
    && apt-get install -y build-essential libpq-dev gettext curl \
    && apt-get clean

# تنظيف إضافي لتقليل الحجم
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# نسخ ملف المتطلبات من repo (نفس أسلوب GitHub/Render)
COPY requirements.txt .

# تثبيت المتطلبات
RUN pip install --no-cache-dir -r requirements.txt

# نسخ المشروع بالكامل
COPY . .

# إدخال سكريبت التشغيل entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

# فتح المنفذ
EXPOSE 8000
