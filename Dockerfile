#Dockerfile

# Pull base image
FROM python:3.8.3-alpine

# Env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work derictory
WORKDIR /src/

# pcyorg deps
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev zlib-dev jpeg-dev

# To install Pillow
ENV LIBRARY_PATH=/lib:/usr/lib

# Install depedencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./app .

# from .env
ENV DEBUG=1
ENV SECRET_KEY="iy2f@xg(i+xh#!62+#h^8ghkb4#q0x)x4jx354a^0_8qf@jp66"
ENV DJANGO_ALLOWED_HOSTS=localhost
ENV SQL_ENGINE=django.db.backends.postgresql
ENV SQL_DATABASE=main
ENV SQL_USER=velnbur
ENV SQL_PASSWORD=velnbur
ENV SQL_HOST=db
ENV SQL_PORT=5432
ENV EMAIL_HOST=email
ENV EMAIL_PASSWORD=password

RUN touch db.sqlite3
RUN python3 manage.py migrate
RUN python3 manage.py makemigrations
RUN python3 manage.py runserver