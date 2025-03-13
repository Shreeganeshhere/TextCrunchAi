from backend.src.main import app
import pytest
from fastapi.testclient import TestClient
import time

client = TestClient(app)

def test_performance():
    """Test for performance of the api"""
    start = time.time()
    text = """Technology is evolving at an unprecedented pace, transforming the way we live, work, and communicate. From artificial intelligence and machine learning to cloud computing and blockchain, innovations are reshaping industries and redefining possibilities. The rise of automation is streamlining workflows, while advancements in AI are pushing the boundaries of what machines can achieve.

As data becomes the new currency, cybersecurity and ethical AI development are more critical than ever. With every breakthrough, new challenges emerge—balancing innovation with responsibility remains a key focus for developers, engineers, and researchers. The future of tech isn’t just about creating smarter systems; it’s about ensuring those systems work for the betterment of society."""
    response = client.post("/summarize",json={"text": text})
    end = time.time()
    assert end - start < 3