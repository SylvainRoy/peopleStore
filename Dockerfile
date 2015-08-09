FROM python:latest
MAINTAINER Sylvain Roy "sylvain.roy@m4x.org"
ENV REFRESHED_AT 09aug15

RUN pip install flask

MKDIR /var/peoplestore
ADD app.py /var/peoplestore
ADD templates /var/peoplestore

CMD python /var/peoplestore/app.py

EXPOSE 5000
