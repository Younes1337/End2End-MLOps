import pytest
from src.app import app
import mlflow 

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Scientific Article Assistant" in response.data

def test_chatbot_response(client):
    response = client.get("/get?msg=Q:%20Can%20you%20give%20me%20an%20abstract%20for%20my%20research%20paper%20with%20the%20Title:A%20Comprehensive%20Overview%20of%20Software%20Development%20in%20BERT-mode?")
    assert response.status_code == 200
    assert b"A: Abstract:" in response.data


# -------------------------------------------------------------- Check MLflow-Databricks Connection ------------------------------------------------------------------------------ 

@pytest.fixture
def databricks_connection():
    # Set the Databricks host URL
    DATABRICKS_HOST = "https://community.cloud.databricks.com/"

    # Configure Databricks
    mlflow.set_tracking_uri(DATABRICKS_HOST)
    yield
    # Clean up (optional)

def test_mlflow_databricks_connection(databricks_connection):
    # This test will run with the configured Databricks connection (run configure_databricks_and_mlflow.sh script to set the credentials before running unit test)
    experiment_name = "/Users/younesmamma20@gmail.com/GPT2-LLM-FineTuning"
    experiment = mlflow.get_experiment_by_name(experiment_name)
    assert experiment is not None

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Add more tests for other routes and app behavior
