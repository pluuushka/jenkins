from flask import Flask
import os
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app) # give back metrics on http://localhost/metrics


@app.route('/')
def hello():
    return "Hello, DevOps! I'm running in a container."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)