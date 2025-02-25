from fastapi import FastAPI
from pydantic import BaseModel
from model.summarizer import Summarizer

app = FastAPI()

class SummarizationText(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Welcome to TextCrunchAI"}

@app.post("/summarize")
def summarize(request: SummarizationText):
    summarizer = Summarizer()
    summary = summarizer.extractive_summarisation(request.text)
    return {"summary": summary}
