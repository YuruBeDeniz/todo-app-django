FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY wait-for-it.sh /app/wait-for-it.sh

COPY requirements.txt .

RUN pip install -r requirements.txt && pip freeze

COPY . .

EXPOSE 8000

CMD ["bash", "-c", "./wait-for-it.sh db:5432 -- python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
