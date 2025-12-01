# ------------------------------
# Stage 1: Builder
# ------------------------------
FROM python:3.12-slim AS builder

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies into /install
RUN pip install --prefix=/install --no-cache-dir -r requirements.txt

# ------------------------------
# Stage 2: Final image
# ------------------------------
FROM python:3.12-slim

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /install /usr/local

# Copy app source code
COPY . .

# Set default command (adjust as needed)
CMD ["python", "app.py"]
