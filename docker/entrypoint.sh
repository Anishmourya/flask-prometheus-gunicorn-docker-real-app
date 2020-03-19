#!/bin/sh

DEFAULT_GUNICORN_CONF=/gunicorn_conf.py
export GUNICORN_CONF=${GUNICORN_CONF:-$DEFAULT_GUNICORN_CONF}
export  prometheus_multiproc_dir="/tmp"

exec gunicorn  app:app -b 0.0.0.0:5000 -c "$GUNICORN_CONF" -w 3 --worker-class gevent