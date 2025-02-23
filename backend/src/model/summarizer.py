from sumy.parsers.plaintext import PlaintextParser  
from sumy.nlp.tokenizers import Tokenizer 
from sumy.summarizers.text_rank import TextRankSummarizer 
from sumy.summarizers.lsa import LsaSummarizer 
import sys, os

# change the cwd to the such that the backend/src is in the sys.path
project_root = os.path.abspath(os.path.join(os.getcwd(), 'backend', 'src'))
sys.path.append(project_root)
print(os.getcwd())

from utils.logger import logger, setup_logger


# extractive summarizaition of text using TextRank algorithm
class Summarizer:
    def __init__(self, summarizer_obj: str = "extractive"):
        """Initializes the summarizer object

        Args:
            text (str): The input text
            summarizer_obj (str, optional): type of summarizer (abstractive or extractive). Defaults to "extractive".
        """
        logger = setup_logger()
        self.summarizer_obj = summarizer_obj
        logger.info(f"Initializing {summarizer_obj} summarizer")

        try:
            if self.summarizer_obj == "extractive":
                self.summarizer = TextRankSummarizer()
                logger.info("TextRank summarizer initialized")
            elif self.summarizer_obj == "abstractive":
                logger.info("Model summarizer initialized")

        except Exception as e:
            logger.error(f"Error initializing summarizer {str(e)}")


    def extractive_summarisation(self,text: str, num_sentences: int = 3, language: str = 'english') -> str:
        """Generates an extractive summary of the text using the TextRank algorithm

        Args:
            text (str): The input text to summarize
            num_sentences (int, optional): The number of sentences in the summary. Defaults to 3.

        Returns:
            str: the extractive summary containing the most 
        """
        try:
           
            parser = PlaintextParser.from_string(text, Tokenizer(language)) # converts the text into a sumy understandable format
           
            summary = self.summarizer(parser.document, num_sentences) # Generating summary containing the top-ranked sentences
            summary = " ".join(str(sentence) for sentence in summary )  # converting the list of sentences into a single text summary
            
            logger.info(f"Extractive summary generated: {summary}") # logging in the summary

        except Exception as e:
            logger.error(f"Error in generating extractive summary: {str(e)}")
            summary = ""
        return summary 

if __name__ == '__main__':
    text = """Artificial Intelligence (AI) is no longer a futuristic concept—it’s part of our daily lives. From voice assistants helping us schedule meetings to AI-powered recommendation systems curating personalized content, its impact is everywhere.

In healthcare, AI is transforming diagnostics, enabling early disease detection through medical imaging. Self-driving cars are another breakthrough, using AI to analyze road conditions and make split-second decisions. Even customer service has evolved, with chatbots handling inquiries more efficiently than ever before.

As AI continues to advance, ethical considerations become crucial. Balancing automation with human oversight will shape how we integrate AI responsibly into society. One thing is certain: AI is here to stay, and its possibilities are limitless."""
    
summarizer = Summarizer()
summary = summarizer.extractive_summarisation(text)
print(summary)
