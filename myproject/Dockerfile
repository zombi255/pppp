# ------------------------------
# Stage 1: Build dependencies
# ------------------------------
FROM python:3.12-slim-bullseye AS builder

# منع ملفات المؤقتات لتوفير المساحة
ENV PIP_NO_CACHE_DIR=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# نسخ ملف المتطلبات أولاً لتقليل إعادة البناء
COPY requirements.txt .

# تحديث pip قبل التثبيت
RUN python -m pip install --upgrade pip

# تثبيت الحزم في مجلد المستخدم لتجنب مشاكل المساحة
RUN pip install --user -r requirements.txt

# ------------------------------
# Stage 2: Final image
# ------------------------------
FROM python:3.12-slim-bullseye

WORKDIR /app

# نسخ الحزم المثبتة من مرحلة البناء
COPY --from=builder /root/.local /root/.local

# أضف مسار الحزم المثبتة في PATH
ENV PATH=/root/.local/bin:$PATH

# نسخ باقي ملفات المشروع
COPY . .

# الأمر الافتراضي لتشغيل التطبيق
CMD ["python", "app.py"]
