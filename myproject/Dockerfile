# myproject/Dockerfile
FROM python:3.11-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
        gettext \
        curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN useradd --create-home appuser

# نسخ ملف المتطلبات الصحيح بالنسبة للـ build context
COPY ./requirements.txt ./
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# نسخ باقي المشروع
COPY . .

# جمع ملفات static
RUN python manage.py collectstatic --noinput --settings=myproject.settings

RUN chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "myproject.wsgi:application"]
