import pytest
from src.model.summarizer import Summarizer

def test_extractive_summarisation():
    """Test for extractive summarization"""
    data = 'This is a test document'
    summarizer = Summarizer()
    summary = summarizer.extractive_summarisation(data)
    assert summary == data
    