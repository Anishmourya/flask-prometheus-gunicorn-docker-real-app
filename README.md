# Flask prometheus gunicorn docker real app
**Python 3.7**

# Docker build
``` 
$ docker build -t anishdhanka/flask_prometheus -f docker/Dockerfile .
```

# Docker run
``` 
$ docker run  -d -p 5000:5000 -td anishdhanka/flask_prometheus 
```

# Request metrics test
```
$ curl -i http://0.0.0.0:5000/metrics
```

# Sample Response
```
# HELP request_count_total Multiprocess metric
# TYPE request_count_total counter
request_count_total{endpoint="/metrics",http_status="200",method="GET",prometheus_app="prometheus_app"} 16.0
# HELP request_latency_seconds Multiprocess metric
# TYPE request_latency_seconds histogram
request_latency_seconds_sum{app_name="prometheus_app",endpoint="/metrics"} 0.014453649520874023
request_latency_seconds_bucket{app_name="prometheus_app",endpoint="/metrics",le="0.005"} 16.0
request_latency_seconds_bucket{app_name="prometheus_app",endpoint="/metrics",le="0.01"} 16.0
request_latency_seconds_bucket{app_name="prometheus_app",endpoint="/metrics",le="0.025"} 16.0
request_latency_seconds_bucket{app_name="prometheus_app",endpoint="/metrics",le="0.05"} 16.0
request_latency_seconds_bucket{app_name="prometheus_app",endpoint="/metrics",le="0.075"} 16.0
request_latency_seconds_bucket{app_name="prometheus_app",endpoint="/metrics",le="0.1"} 16.0
request_latency_seconds_bucket{app_name="prometheus_app",endpoint="/metrics",le="0.25"} 16.0
request_latency_seconds_bucket{app_name="prometheus_app",endpoint="/metrics",le="0.5"} 16.0
request_latency_seconds_bucket{app_name="prometheus_app",endpoint="/metrics",le="0.75"} 16.0
request_latency_seconds_bucket{app_name="prometheus_app",endpoint="/metrics",le="1.0"} 16.0
request_latency_seconds_bucket{app_name="prometheus_app",endpoint="/metrics",le="2.5"} 16.0
request_latency_seconds_bucket{app_name="prometheus_app",endpoint="/metrics",le="5.0"} 16.0
request_latency_seconds_bucket{app_name="prometheus_app",endpoint="/metrics",le="7.5"} 16.0
request_latency_seconds_bucket{app_name="prometheus_app",endpoint="/metrics",le="10.0"} 16.0
request_latency_seconds_bucket{app_name="prometheus_app",endpoint="/metrics",le="+Inf"} 16.0
request_latency_seconds_count{app_name="prometheus_app",endpoint="/metrics"} 16.0
```