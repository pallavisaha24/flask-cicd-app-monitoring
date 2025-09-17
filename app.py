from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

# Attach Prometheus metrics to Flask app
metrics = PrometheusMetrics(app)

@app.route('/')
def hello():
    return "Hello from Flask CI/CD with Prometheus!"

@app.route('/health')
def health():
    return {"status": "UP"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

