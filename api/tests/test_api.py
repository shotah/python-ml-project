import pytest
from api.api import app


@pytest.fixture(autouse=True)
def client():
    with app.test_client() as client:
        yield client

def test_answer_question_valid_query(client):
    data = {"query": "What is the capital of France?"}
    response = client.post("/api/answer", json=data)
    assert response.status_code == 200
    assert response.json["answer"] == "Paris"  # Or your expected answer

def test_answer_question_missing_query(client):
    response = client.post("/api/answer", json={})  # Missing query
    assert response.status_code == 400
    assert "Missing 'query' parameter" in response.json["error"]

# Add more test cases for different scenarios, error conditions, etc.