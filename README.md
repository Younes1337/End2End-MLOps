# MLOps Project
 
<p align="center">
  <img src="https://www.vectorlogo.zone/logos/docker/docker-icon.svg" alt="Docker" width="50" height="50" />
  <img src="https://www.vectorlogo.zone/logos/amazon_aws/amazon_aws-icon.svg" alt="Amazon S3" width="50" height="50" />
  <img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" alt="Flask" width="50" height="50" />
 <a href="https://cdnlogo.com/logo/data-version-control_134778.html"><img src="https://www.cdnlogo.com/logos/d/2/data-version-control.svg"  width="50" height="50"></a>
<a title="Jason Long, CC BY 3.0 &lt;https://creativecommons.org/licenses/by/3.0&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Git-logo.svg"><img width="90" alt="Git-logo" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Git-logo.svg/512px-Git-logo.svg.png"></a>
  <a title="Amazon.com, Inc., Public domain, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Amazon-S3-Logo.svg"><img width="50" alt="Amazon-S3-Logo" src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Amazon-S3-Logo.svg/256px-Amazon-S3-Logo.svg.png"></a>
 <img src="https://www.vectorlogo.zone/logos/gitlab/gitlab-icon.svg" alt="GitLab" width="50" height="50" />
  <img src="https://www.vectorlogo.zone/logos/grafana/grafana-icon.svg" alt="Grafana" width="50" height="50" />
</p>

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
- Model training and deployment with Amazon SageMaker 🏭

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
- Amazon SageMaker 🏭 - a fully managed service for building, training, and deploying machine learning models.

## Architecture
Describe your MLOps project's high-level architecture here. You can use diagrams or text to provide an overview of how different components interact and how data flows through the pipeline.
<p align="center">
  <img src="./mlops.png" alt="Image Description" style="border-radius: 50%;" />
</p>




## Getting Started
To get started with this project, follow these instructions to set up your environment and start working with the MLOps pipeline.

### Installation
```bash
# Clone the repository to your local machine
git clone https://github.com/your-username/mlops-project.git
cd mlops-project

# Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # For Windows, use: venv\Scripts\activate

# Install the required dependencies
pip install -r requirements.txt
```
### Project Structure
```bash
|-- mlops_project/
    |-- data/
    |-- models/
    |-- notebooks/
    |-- scripts/
    |-- tests/
    |-- config/
    |-- README.md
    |-- requirements.txt
    |-- .gitignore

```
[Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
