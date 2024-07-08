FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
USER root
RUN sudo apt-get update
RUN useradd -ms /bin/bash newuser
USER newuser
WORKDIR /usr/src/jjj

COPY ./requirements.txt /usr/requirements.txt
RUN pip install -r /usr/requirements.txt

COPY . /usr/src/jjj
