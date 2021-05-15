import logging
from flask import Flask
from flask import jsonify
from prometheus_flask_exporter import PrometheusMetrics

logging.basicConfig(level=logging.INFO)
logging.info("Setting LOGLEVEL to INFO")
app = Flask(__name__)

metrics = PrometheusMetrics(app)
metrics.info("app_info", "App Info, this can be anything you want", version="1.0.0")
metrics.start_http_server(5099)


@app.route("/flask-prometheus-grafana-example/")
def hello():
    return jsonify(say_hello())


@app.route("/")
def say_hello():
    return {"message": "hello"}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
