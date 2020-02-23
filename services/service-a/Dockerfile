FROM ubuntu:16.04

MAINTAINER Adir Atias "atias.adir@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN apt-get update && apt-get -qy install python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . /app

RUN apt-get update && apt-get -qy install wget iputils-ping
RUN groupadd -g 999 appuser && \
	useradd -r -u 999 -g appuser appuser
USER appuser

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]