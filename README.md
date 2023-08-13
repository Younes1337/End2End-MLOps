<!-- Logo, Title, and Badges Section -->
<p align="center">
  <a>
    <img src="./logo-white.png" width="150" height="150">
  </a>
</p>

<h1 align="center">End-to-End MLOps: From Data to Deployment</h1>

<p align="center">
  <a href="https://www.python.org/">
    <img alt="Python Version" src="https://img.shields.io/badge/Python-3.7%2B-informational">
  </a>
  <a href="https://github.com/Younes1337/End2End-MLOps">
    <img alt="GitHub Repo" src="https://img.shields.io/badge/GitHub-Repo-blue">
  </a>
  <a href="https://www.docker.com/">
    <img alt="Docker" src="https://img.shields.io/badge/Docker-Latest-blue">
  </a>
  <a href="https://www.tensorflow.org/">
    <img alt="TensorFlow" src="https://img.shields.io/badge/TensorFlow-2.x-orange">
  </a>
  <a href="https://jupyter.org/">
    <img alt="Jupyter" src="https://img.shields.io/badge/Jupyter-Latest-orange">
  </a>
</p>

<p align="center">
  <img src="https://www.vectorlogo.zone/logos/docker/docker-icon.svg" alt="Docker" width="50" height="50" />
  <img src="https://www.vectorlogo.zone/logos/amazon_aws/amazon_aws-icon.svg" alt="Amazon S3" width="50" height="50" />
  <img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" alt="Flask" width="50" height="50" />
  <a href="https://cdnlogo.com/logo/data-version-control_134778.html">
    <img src="https://www.cdnlogo.com/logos/d/2/data-version-control.svg" width="50" height="50">
  </a>
  <a title="Jason Long, CC BY 3.0 <https://creativecommons.org/licenses/by/3.0>, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Git-logo.svg">
    <img width="90" alt="Git-logo" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Git-logo.svg/512px-Git-logo.svg.png">
  </a>
  <img src="https://www.vectorlogo.zone/logos/gitlab/gitlab-icon.svg" alt="GitLab" width="50" height="50" />
  <img src="https://www.vectorlogo.zone/logos/grafana/grafana-icon.svg" alt="Grafana" width="50" height="50" />
  <a title="Apache Software Foundation, Apache License 2.0 &lt;http://www.apache.org/licenses/LICENSE-2.0&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Apache_kafka.svg"><img width="50" alt="Apache kafka" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Apache_kafka.svg/128px-Apache_kafka.svg.png"></a>
  <a title="Snowflake, Public domain, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Snowflake_Logo.svg"><img width="128" alt="Snowflake Logo" src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Snowflake_Logo.svg/128px-Snowflake_Logo.svg.png"></a>
  

</p>

<!-- Divider -->
<hr>

## Introduction
Welcome to the MLOps project! This repository aims to showcase a comprehensive MLOps implementation, enabling smooth and efficient development, deployment, and maintenance of machine learning models. MLOps is the practice of integrating machine learning workflows with DevOps practices, ensuring reproducibility, scalability, and automation throughout the model's lifecycle.

## Project Overview
The MLOps project provides a structured and organized pipeline for machine learning projects, covering the entire workflow from data preprocessing to model deployment. The primary goal is to streamline collaboration among data scientists, machine learning engineers, and operations teams, leading to a more efficient and reliable model deployment process.

## 🚀 Features
- Data versioning and management using DVC 📊
- Unit testing and integration testing with pytest 🧪
- Model serving and API creation with Flask 🤖
- Containerization and deployment with Docker 🐳
- Cloud infrastructure and deployment on Amazon EC2 ☁️
- Monitoring and visualization with Grafana 📈
- Version control and continuous integration with GitLab 🔧

## Tech Stack
The MLOps project utilizes the following main tools and libraries:

- TensorFlow 🧠 - an open-source machine learning library.
- Scikit-learn 📚 - a machine learning library for Python.
- MLflow 📦 - an open-source platform for the complete machine learning lifecycle.
- DVC 📈 - a version control system for data sets and machine learning models.
- Pytest 🧪 - a testing framework for Python.
- Flask 🤖 - a lightweight web framework for creating APIs.
- Docker 🐳 - containerization platform for packaging applications.
- Amazon EC2 ☁️ - cloud-based virtual machines for deployment.
- Grafana 📈 - a monitoring and observability platform.
- GitLab 🔧 - version control and continuous integration platform.

## Prerequisites

Before you begin, make sure you have the following in place:

- **AWS Account:** You need an AWS account to access EC2, ECR, and S3 services.
- **Docker:** Make sure you have Docker installed on your local machine.
- **Python:** Ensure you have Python (version 3.6 or higher) and pip installed.

## Setup
Navigate to the project directory.

1. **Configure AWS Credentials:**

Set up your AWS credentials on your local machine. You can do this by installing the AWS Command Line Interface (CLI) and running the `aws configure` command, providing your AWS Access Key ID, Secret Access Key, and default region.

Navigate to the project directory.


2. **Build Docker Image and Push to ECR:**

- Ensure you have Docker running on your local machine.

- Create an Amazon ECR repository using the AWS Management Console or the AWS CLI.

- Build the Docker image:

  ```
  docker build -t project-name .
  ```

  Replace `project-name` with a suitable name for your Docker image.

- Tag the Docker image with the ECR repository URI:

  ```
  docker tag project-name:latest <aws_account_id>.dkr.ecr.<region>.amazonaws.com/project-repo:latest
  ```

  Replace `<aws_account_id>` with your AWS account ID, `<region>` with the AWS region you want to use, and `project-repo` with the name of the ECR repository you created.

- Log in to the ECR registry:

  ```
  aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.<region>.amazonaws.com
  ```

  Replace `<region>` with the AWS region you want to use, and `<aws_account_id>` with your AWS account ID.

- Push the Docker image to ECR:

  ```
  docker push <aws_account_id>.dkr.ecr.<region>.amazonaws.com/project-repo:latest
  ```

  Replace `<region>` with the AWS region you want to use, `<aws_account_id>` with your AWS account ID, and `project-repo` with the name of the ECR repository you created.

3. **Set up S3 Bucket:**

- Create an S3 bucket using the AWS Management Console or the AWS CLI.

- Note down the name of the S3 bucket, as it will be used later.

4. **EC2 Instance Setup:**

- Launch an EC2 instance in your AWS account using the AWS Management Console or the AWS CLI.

- Choose an appropriate instance type and Amazon Machine Image (AMI) with Docker pre-installed.

- Make sure to configure the security groups to allow access to the necessary ports (e.g., SSH, HTTP).

- Once the instance is running, note down its public IP address or DNS name.

5. **SSH into the EC2 Instance:**

Use SSH to connect to the EC2 instance:

Replace `path/to/your/key.pem` with the path to your SSH private key and `ec2-instance-public-ip` with the public IP address or DNS name of the EC2 instance.

## Running the Project

Now that you have set up the Docker image on ECR and launched the EC2 instance, follow the steps below to run the project:

1. **SSH into the EC2 Instance:**

If you haven't already done so, use SSH to connect to the EC2 instance as described in step 7 above.

2. **Pull the Docker Image:**

Pull the Docker image from ECR onto the EC2 instance


Replace `<aws_account_id>` with your AWS account ID, `<region>` with the AWS region you used, and `project-repo` with the name of the ECR repository.

3. **Run the Docker Container:**

Run the Docker container on the EC2 instance:


Replace `<aws_account_id>` with your AWS account ID, `<region>` with the AWS region you used, and `project-repo` with the name of the ECR repository.

4. **Access the Web Application:**

The Docker container should now be running the web application on port 80. Open a web browser and enter the public IP address or DNS name of the EC2 instance to access the web application.


## Versions

| Technology   | Version |
|--------------|---------|
| Python       | 3.9     |
| Docker       | 20.10   |
| AWS CLI      | 2.2.14  |


## Architecture

<p align="center">
  <img src="./mlops.png" alt="Image Description" style="border-radius: 50%;" />
</p>

## Data Source
<p align="center">
  <img src="./Data Source.png" alt="Image Description" style="border-radius: 30%;" />
</p>



## Getting Started
To get started with this project, follow these instructions to set up your environment and start working with the MLOps pipeline.

### Installation
```bash
# Clone the repository to your local machine
git clone https://github.com/Younes1337/End2End-MLOps.git
cd End2End-MLOps

# Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # For Windows, use: venv\Scripts\activate

# Install the required dependencies
pip install -r requirements.txt
```
### Project Structure
```bash
📁 MLOps_project/
│
├── README.md
├── requirements.txt
├── .gitignore
├── Dockerfile 🐳
├── docker-compose.yml 🐳
│
├── 📁 src/
│   ├── __init__.py
│   ├── app.py
│   ├── 📁 data/
│   │   └── (data loading and preprocessing scripts)
│   ├── 📁 models/
│   │   └── (machine learning models and related scripts)
│   ├── 📁 utils/
│   │   └── (utility functions and helper scripts)
│   └── mlflow_server.py
│
├── 📁 tests/ 🧪
│   ├── __init__.py
│   ├── test_app.py
│   ├── test_data.py
│   ├── test_models.py
│   └── test_utils.py
│
├── 📁 experiments/ 🧪
│   ├── 📁 experiment_1/
│   │   └── 📁 mlruns/
│   └── 📁 experiment_2/
│       └── 📁 mlruns/
│
├── 📁 config/ ⚙️
│   ├── config.yaml
│   └── logging.yaml
│
├── 📁 logs/ 📜
│   └── (log files)
│
├── 📁 dashboards/ 📊
│   └── (Grafana dashboard configurations)
│
├── 📁 deployment/ 🚀
│   ├── nginx.conf
│   ├── supervisor.conf
│   └── app.service
│
└── 📁 scripts/ 🛠️
    ├── setup.sh
    ├── deploy.sh
    └── run_tests.sh



```
## Contributing

If you would like to contribute to this project, please fork the repository, make your changes, and submit a pull request. 
We welcome contributions from the community!
