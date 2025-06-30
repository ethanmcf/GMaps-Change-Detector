# GMaps-Change-Detector

## Setup

Create gcp service account, add storage admin role. Save key as goog_cred_key.json in root dir
Setup supabase psql
Create env file and then create secrets key
EMAIL_RECIPIENTS
SENDER_EMAIL=
SENDER_PASSWORD=
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=465
PSQL_URL=
PSQL_KEY=
GOOGLE_APPLICATION_CREDENTIALS=google_cred_key.json

## Run locally

```
docker build -t gmaps-detector .
docker run --env-file .env gmaps-detector
```

## Run Kubernetes cronjob

```
minikube start # if not already running
kubectl get namespace # Verify gmaps-detector namespace
kubectl create namespace gmaps-detector
docker build -t gmaps-detector .
minikube image load gmaps-detector
kubectl apply -f k8s --recursive -n gmaps-detector

kubectl get pods -n gmaps-detector
kubectl logs POD_NAME -n gmaps-detector
```

# Load secrets from .env
