FROM python:3.7-alpine3.15
MAINTAINER Anish Dhanka <anish.mourya5@gmail.com>

# add gcc for gevent
RUN apk add --no-cache gcc musl-dev

RUN apk add py-gunicorn
# pip cache for docker build
COPY requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
COPY docker/gunicorn_conf.py /gunicorn_conf.py

WORKDIR /app
COPY . /app/
ENV PYTHONPATH=/app

ENTRYPOINT ["/entrypoint.sh"]
