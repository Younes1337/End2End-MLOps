import pytest
from src.app import app

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

# Add more tests for other routes and app behavior
