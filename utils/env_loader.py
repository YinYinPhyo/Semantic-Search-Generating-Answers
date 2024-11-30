import os
from dotenv import load_dotenv, find_dotenv

def load_environment():
    """Load environment variables from .env file"""
    _ = load_dotenv(find_dotenv())
    return os.environ.get('COHERE_API_KEY') 