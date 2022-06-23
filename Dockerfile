FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/cinema

RUN apt update && apt -y install gettext

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt

RUN mkdir /usr/src/cinema/static
RUN mkdir /usr/src/cinema/media

COPY . .



