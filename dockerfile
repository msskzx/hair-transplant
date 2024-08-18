
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py migrate

EXPOSE 8080

CMD ["python", "manage.py" "runserver", "0.0.0.0:8080"]