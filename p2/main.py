from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

api = Flask(__name__)
metrics = PrometheusMetrics(api)
metrics.info("app_info", "App Info, this can be anything you want", version="1.0.0")


@app.route('/')
def hello():
    return "Hello World! its P2"

@app.route('/start')
def hello():
    return "Hello World! its start"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
