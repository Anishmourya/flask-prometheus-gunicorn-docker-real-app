"""
Flask prometheus gunicorn docker real app
https://github.com/prometheus/client_python#multiprocess-mode-gunicorn
"""

from flask import Flask
from flask import jsonify
from flask import Response
from flask import request
from flask import make_response
from prometheus_client import Counter
from prometheus_client import Histogram
from prometheus_client import multiprocess
from prometheus_client import CollectorRegistry
from prometheus_client import generate_latest
import time

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "request_count",
    "App Request Count",
    ["prometheus_app", "method", "endpoint", "http_status"],
)
REQUEST_LATENCY = Histogram(
    "request_latency_seconds", "Request latency", ["app_name", "endpoint"]
)
CONTENT_TYPE_LATEST = str("text/plain; version=0.0.4; charset=utf-8")


@app.before_request
def before_request():
    request.start_time = time.time()


@app.after_request
def after_request(response):
    resp_time = time.time() - request.start_time
    REQUEST_COUNT.labels(
        "prometheus_app", request.method, request.path, response.status_code
    ).inc()
    REQUEST_LATENCY.labels("prometheus_app", request.path).observe(resp_time)
    return response


@app.route("/")
def home():
    return make_response(jsonify({"status": "ok"}), 200)


@app.route("/metrics")
def metrics():
    registry = CollectorRegistry()
    multiprocess.MultiProcessCollector(registry)
    data = generate_latest(registry)
    return Response(data, mimetype=CONTENT_TYPE_LATEST)


if __name__ == "__main__":
    app.run()
