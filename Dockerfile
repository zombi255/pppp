FROM python:3.12-slim

# Working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# --------------------------
# FIXED: requirements path
# --------------------------
# Copy requirements FIRST (better Docker cache)
COPY myproject/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy all project files
COPY myproject/ /app/

# --------------------------
# Entrypoint
# --------------------------
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

# --------------------------
# Render command
# --------------------------
# Render sets $PORT automatically
CMD ["sh", "-c", "gunicorn myproject.wsgi:application --bind 0.0.0.0:$PORT"]
