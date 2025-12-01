# استخدم هذا كـ myproject/Dockerfile
FROM python:3.11-slim-bullseye

WORKDIR /app

# انسخ dependencies من نفس المجلد
COPY requirements.txt ./

RUN python -m pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# انسخ باقي المشروع
COPY . .

# جمع الملفات الثابتة
RUN python manage.py collectstatic --noinput --settings=myproject.settings || true

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "myproject.wsgi:application"]
