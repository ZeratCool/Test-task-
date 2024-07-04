FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN useradd -ms /bin/bash newuser
WORKDIR /usr/src/proj

COPY requirements.txt /usr/src/proj/requirements.txt
RUN pip install --no-cache-dir -r /usr/src/proj/requirements.txt

COPY .docker.env /usr/src/proj/.docker.env
COPY . /usr/src/proj

USER newuser
