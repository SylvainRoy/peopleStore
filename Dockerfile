FROM python:2.7
MAINTAINER Sylvain Roy "sylvain.roy@m4x.org"
ENV REFRESHED_AT 09aug15

RUN pip install flask

RUN mkdir /var/peoplestore
ADD . /var/peoplestore

WORKDIR /var/peoplestore
CMD python /var/peoplestore/app.py

EXPOSE 80