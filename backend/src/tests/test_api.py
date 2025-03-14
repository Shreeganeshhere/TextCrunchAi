import pytest
from backend.src.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_home():
    """Test for home route"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to TextCrunchAI"}


def test_summarize_api():
    """Test for summarize API"""
    response = client.post("/summarize",json={"text": "This is a test document for summarization."})
    assert response.status_code == 200
    assert "summary" in response.json()


def test_upload_api():
    """Test for upload API"""
    files = {"file": ("test.txt", "This is a test file.", "text/plain")}
    response = client.post("/upload", files=files)
    assert response.status_code == 200
    assert "message" in response.json()


def test_invalid_request():
    """Test for invalid request"""
    response = client.post("/summarize", json={"text": ""})
    assert response.status_code ==  422
    