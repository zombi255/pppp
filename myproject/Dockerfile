FROM python:3.11-slim-bullseye

# Prevent Python from writing .pyc files and enable unbuffered output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
        gettext \
        curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user
RUN useradd --create-home appuser

# Copy and install Python dependencies first to leverage layer caching
COPY requirements.txt ./
RUN python -m pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Collect static files (adjust settings module if needed)
RUN python manage.py collectstatic --noinput --settings=myproject.settings || true

# Ensure permissions for the appuser
RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 8000

# Default command — run Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "myproject.wsgi:application"]
Use an official Python runtime as base image,
FROM python:3.11-slim-bullseye

Set work directory,
WORKDIR /app

Install system dependencies,
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
        gettext && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

Copy requirements file,
COPY requirements.txt .

Install Python dependencies,
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

Copy project,
COPY . .

Create static files directory and set permissions,
RUN mkdir -p /app/staticfiles && \
    chmod 755 /app/staticfiles

Collect static files,
RUN python manage.py collectstatic --noinput --settings=myproject.settings


Create superuser (optional - remove in production),
RUN echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')" | python manage.py shell --settings=myproject.settings,
Expose port,
EXPOSE 8000

Run application,
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "myproject.wsgi:application"]