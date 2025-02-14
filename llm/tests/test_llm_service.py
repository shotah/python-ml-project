import pytest
import json
from ..llm_service import app

@pytest.fixture(autouse=True)
def client():
    with app.test_client() as client:
        yield client

def test_generate_text_valid_prompt(client):
    response = client.post(
        '/llm/generate',
        json={'prompt': 'Write a short test poem about Seattle'}
    )
    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    assert 'response' in data
    assert isinstance(data['response'], str)
    assert len(data['response']) > 0

def test_generate_text_missing_prompt(client):
    response = client.post(
        '/llm/generate',
        json={}  # Missing 'prompt'
    )
    assert response.status_code == 400
    data = json.loads(response.data.decode('utf-8'))
    assert 'error' in data
    assert data['error'] == "Missing 'prompt' parameter"

def test_generate_text_empty_prompt(client):
    response = client.post(
        '/llm/generate',
        json={'prompt': ''}  # Empty prompt
    )
    assert response.status_code == 400 # Or you might expect 400, adjust assertion if needed
    data = json.loads(response.data.decode('utf-8'))
    assert "error" in data
    assert isinstance(data['error'], str)
    # You might want to assert something about the response content for an empty prompt
    # For now, just checking for a valid response.