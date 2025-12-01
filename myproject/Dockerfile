# مرحلة build
FROM python:3.12-slim AS build

WORKDIR /app
COPY requirements.txt .
RUN pip install --prefix=/install --no-cache-dir -r requirements.txt

COPY . .

# المرحلة النهائية
FROM python:3.12-slim
WORKDIR /app
COPY --from=build /install /usr/local
COPY --from=build /app /app

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]
