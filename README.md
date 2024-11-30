# Semantic-Search-Generating-Answers

This project provides a question-answering system inspired by Andrew Ng's article on building a career in AI. It utilizes Cohere's language models for embedding generation and text responses, alongside the Annoy library for efficient similarity search.

---

## Features

- Preprocessing and cleaning of input text
- Semantic search using embeddings for relevance
- Contextual question answering based on retrieved data
- Configurable parameters for search and text generation
- Modular architecture designed for extensibility
- Comprehensive testing with multiple predefined test cases
- Clear and formatted result display

---

## Prerequisites

- Python version 3.7 or higher
- Pip (Python package installer)
- A valid Cohere API key, which can be obtained at [Cohere's Dashboard](https://dashboard.cohere.ai)

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Set up and activate a virtual environment

    On Unix/macOS
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

    On Windows
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a .env file in the root directory with the following content:
    ```plaintext
    COHERE_API_KEY=your_api_key_here
    ```

# Configuration
The system's behavior can be modified via the config/config.py file:

- Search Settings:
    - SEARCH_INDEX_FILENAME: File name for storing the search index
    - NUM_TREES: Number of trees in the Annoy index (affects accuracy and - speed)
    - NUM_NEIGHBORS: Number of nearest neighbors to retrieve

- Generation Settings:

    - MAX_TOKENS: Maximum token limit for generated answers
    - MODEL_NAME: Cohere model to be used
    - TEMPERATURE: Creativity setting for generation
    - DEFAULT_NUM_GENERATIONS: Default number of variations for answers

- Test Configuration:

    - Test parameters for various cases, such as technical skills, project guidance, and learning path recommendations.

# Usage
Execute the main script:

```bash
python main.py
```
# Test Cases
The system includes various predefined tests:

1. Single generation for specific topics
2. Multiple variations for career guidance
3. Handling of out-of-domain questions
4. Technical skills evaluation
5. Recommendations for project selection
6. Suggestions for learning paths
7. Analysis of community impact
8. Job search-related guidance

********