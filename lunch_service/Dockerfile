FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN useradd -ms /bin/bash newuser
USER newuser
WORKDIR /usr/src/proj

COPY requirements.txt /usr/requirements.txt
COPY ./.env /usr/src/proj
RUN pip install -r /usr/requirements.txt

COPY . /usr/src/proj