FROM ubuntu:18.04

ARG GIT_USERNAME
ARG GIT_PASSWORD

ENV TZ=Asia/Kolkata

RUN apt-get update && \
    apt-get dist-upgrade --yes && \
	apt-get install -y libpng-dev libjpeg8-dev libfreetype6-dev python3-dev python3-pip libssl-dev libcurl4-openssl-dev git vim && \
	pip3 install --no-cache-dir --upgrade pyinotify && \
	apt-get autoremove -y && apt-get clean -y && \
	pip3 install --upgrade pip && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /root/src/bakery_management/requirements.txt
RUN pip3 install --no-cache-dir --trusted-host pypi.python.org -r /root/src/bakery_management/requirements.txt

ADD . /root/src/bakery_management

ENTRYPOINT /bin/bash

EXPOSE 9101