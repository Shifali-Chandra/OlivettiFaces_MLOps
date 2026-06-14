# Olivetti Faces MLOps Pipeline

Major Assignment for MLOps Course at IIT Jodhpur
By Shifali Chandra - G25AI1040

## Project Overview

This project implements an end-to-end MLOps pipeline using the Olivetti Faces dataset. A Decision Tree Classifier is trained to classify face images, evaluated on a test set, deployed as a Flask web application, containerized using Docker, and deployed on Kubernetes.

## Features

* Train a Decision Tree Classifier on the Olivetti Faces dataset
* Save and load the trained model
* Evaluate model performance using test accuracy
* Flask web application for image upload and prediction
* Dockerized application deployment
* Docker Hub image publishing
* Kubernetes deployment with 3 replicas
* GitHub Actions CI pipeline

## Installation

Clone the repository:

```bash
git clone https://github.com/Shifali-Chandra/OlivettiFaces_MLOps.git
cd OlivettiFaces_MLOps
```

## Branch Usage

### main

Contains project documentation.

### dev

Contains model training, testing, and GitHub Actions workflow.

Switch to dev:

```bash
git checkout dev
```

### docker_cicd

Contains Flask application, Docker, Docker Hub, and Kubernetes deployment files.

Switch to docker_cicd:

```bash
git checkout docker_cicd
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Project

### Train Model

```bash
python train.py
```

Generates:

```text
savedmodel.pth
```

### Evaluate Model

```bash
python test.py
```

Example Output:

```text
Test Accuracy: 0.5333
```

### Run Flask Application
Switch to the docker_cicd branch:

```bash
git checkout docker_cicd
```

Start the application
```bash
python app.py
```

Open:

```text
http://localhost:5000
```

Upload a sample image from sample_images and view the predicted class.

## Docker

Build Docker image:

```bash
docker build -t olivetti-face-app .
```

Run Docker container:

```bash
docker run -p 5000:5000 olivetti-face-app
```

Open:

```text
http://localhost:5000
```

## Docker Hub

Docker Image:

```text
shifalichandra/olivetti-face-app:latest
```

Pull image:

```bash
docker pull shifalichandra/olivetti-face-app:latest
```

Run image:

```bash
docker run -p 5000:5000 shifalichandra/olivetti-face-app:latest
```

## Kubernetes Deployment

Deploy application:

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

Verify deployment:

```bash
kubectl get pods
kubectl get svc
```

Port forward service:

```bash
kubectl port-forward svc/olivetti-service 5000:5000
```

Open:

```text
http://localhost:5000
```

## CI/CD

GitHub Actions workflow automatically:

* Installs dependencies
* Runs train.py
* Generates savedmodel.pth
* Runs test.py
* Validates the project pipeline

## Repository Structure

```text
.
├── app.py
├── train.py
├── test.py
├── requirements.txt
├── Dockerfile
├── deployment.yaml
├── service.yaml
├── savedmodel.pth
├── sample_images/
├── templates/
└── .github/workflows/ci.yml
```