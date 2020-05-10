FROM ubuntu:18.04

RUN apt-get update -y && apt-get upgrade
RUN apt-get install -y python3-pip libhunspell-1.6-0 libhunspell-dev
ENV PYTHONIOENCODING=utf-8
RUN pip3 install cyhunspell
WORKDIR /app
COPY . /app
CMD tail -f /dev/null
