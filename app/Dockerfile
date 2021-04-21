#Dockerfile

# Pull base image
FROM python:3.8.3-alpine

# Env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work derictory
WORKDIR /usr/src/app

# pcyotg deps
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev zlib-dev jpeg-dev

# To install Pillow
ENV LIBRARY_PATH=/lib:/usr/lib

# Install depedencies
RUN pip install --upgrade pip
COPY ./requirments.txt .
RUN pip install -r requirments.txt

COPY . .
