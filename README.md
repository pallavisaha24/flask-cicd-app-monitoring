# Flask CI/CD App with Monitoring

This project demonstrates a complete **CI/CD pipeline** for a Flask application deployed on **Kubernetes**, with monitoring using **Prometheus** and **Grafana**.

## 🚀 Features
- **Flask Application** – Simple Python web app as demo.
- **CI/CD Pipeline** – Automated build, test, and deploy using GitHub/GitLab CI.
- **Dockerized Deployment** – App packaged into Docker image.
- **Kubernetes** – Deployment, Service, and Monitoring stack.
- **Prometheus** – Metrics collection from app and cluster.
- **Grafana** – Visual dashboards for monitoring.

---

## 📂 Project Structure
flask-cicd-app-monitoring/
│── app/ # Flask application code
│── k8s/ # Kubernetes manifests
│ ├── deployment.yaml
│ ├── service.yaml
│ ├── prometheus.yaml
│ ├── grafana.yaml
│── Dockerfile # Build Flask app image
│── requirements.txt # Python dependencies
│── .gitlab-ci.yml # GitLab CI/CD pipeline (if using GitLab)
│── .github/workflows/ci.yml # GitHub Actions pipeline (if using GitHub)
│── README.md # Project documentation

yaml
Copy code

---

## 🛠️ Setup Instructions

### 1. Clone Repo

```bash
git clone https://github.com/<your-username>/flask-cicd-app-monitoring.git
cd flask-cicd-app-monitoring
2. Run Locally (Optional)

bash
Copy code
pip install -r requirements.txt
python app/app.py
Access at: http://localhost:5000

3. Docker Build

Copy code
docker build -t flask-cicd-app:latest .
docker run -p 5000:5000 flask-cicd-app:latest
4. Kubernetes Deployment

Copy Code
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
5. Monitoring Setup

Copy code
kubectl apply -f k8s/prometheus.yaml
kubectl apply -f k8s/grafana.yaml
Prometheus → http://<node-ip>:<prometheus-port>
Grafana → http://<node-ip>:<grafana-port> (default creds: admin/admin)

🔍 Monitoring
Prometheus scrapes metrics from Flask app (/metrics endpoint).
Grafana visualizes dashboards for application and cluster health.

⚡ CI/CD
On each git push, pipeline will:
Run tests
Build & push Docker image
Deploy to Kubernetes

📊 Future Improvements
Add Helm charts for easier deployment.

Implement Alertmanager with Prometheus.

Secure Grafana with OAuth/SSO.
