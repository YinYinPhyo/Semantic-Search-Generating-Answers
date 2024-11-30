#!/usr/bin/env python
# coding: utf-8

#################################################
# Generating Answers
#
# Step 1: Preprocessing input texts
# Step 2: Embeddings
# Step 3: Searching Articles
# Step 4: Generating Answers
#################################################

import warnings
warnings.filterwarnings('ignore')

from utils.env_loader import load_environment
from src.preprocessing.text_processor import TextProcessor
from src.embeddings.embedding_handler import EmbeddingHandler
from src.search.search_engine import SearchEngine
from src.qa.question_answerer import QuestionAnswerer
from data.sample_text import SAMPLE_TEXT
from config.config import *
from utils.display_formatter import DisplayFormatter
from src.test_cases.test_suite import TestSuite

def run_test_cases():
    """Run multiple test cases to demonstrate system capabilities"""
    
    formatter = DisplayFormatter()
    test_suite = TestSuite(qa_system)
    test_suite.run_all_tests(formatter)

def main():
    #################################################
    # Step 1: Preprocessing input texts
    #################################################
    print("Step 1: Processing text...")
    text_processor = TextProcessor()
    processed_texts = text_processor.process_text(SAMPLE_TEXT)
    
    #################################################
    # Step 2: Embeddings
    #################################################
    print("Step 2: Generating embeddings...")
    api_key = load_environment()
    embedding_handler = EmbeddingHandler(api_key)
    embeddings = embedding_handler.get_embeddings(processed_texts)
    
    print("Building search index...")
    search_index = embedding_handler.build_search_index(
        embeddings, 
        NUM_TREES, 
        SEARCH_INDEX_FILENAME
    )
    
    #################################################
    # Step 3: Initialize Search Engine and QA System
    #################################################
    print("Step 3: Initializing search engine...")
    global search_engine, qa_system
    search_engine = SearchEngine(embedding_handler.co, search_index, processed_texts)
    qa_system = QuestionAnswerer(embedding_handler.co, search_engine)
    
    #################################################
    # Step 4: Run Test Cases
    #################################################
    print("Step 4: Running test cases...")
    run_test_cases()

if __name__ == "__main__":
    main()