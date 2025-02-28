import pytest
from src.model.summarizer import Summarizer
from src.main import app

test_sample = """Artificial intelligence is transforming industries by enabling automation and decision-making based on data-driven insights. AI models analyze vast amounts of information quickly and efficiently, making them valuable for various applications such as healthcare, finance, and marketing."""

def test_extractive_summarisation():
    """Test for extractive summarizer"""
    summarizer = Summarizer()
    summary = summarizer.extractive_summarisation(test_sample)
    assert summary not in [None, ""]
    assert "AI" in summary
    
def test_abstractive_summarisation():
    """Test for abstractive summarizer"""
    summarizer = Summarizer()
    summary = summarizer.abstractive_summarisation(test_sample)
    assert summary not in [None, ""]
    assert 'AI' in summary


def hybrid_summarisation():
    """Test for hybrid summarizer"""
    summarizer = Summarizer()
    summary = summarizer.hybrid_summarisation(test_sample)
    assert summary not in [None, ""]
    assert 'AI' in summary
    