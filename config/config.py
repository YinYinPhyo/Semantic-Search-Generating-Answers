#################################################
# Configuration Parameters
#################################################

# Search index configuration
SEARCH_INDEX_FILENAME = 'test.ann'
NUM_TREES = 10
NUM_NEIGHBORS = 10

# Generation configuration
MAX_TOKENS = 70
MODEL_NAME = "command-nightly"
TEMPERATURE = 0.5
DEFAULT_NUM_GENERATIONS = 1

# Embedding configuration
EMBEDDING_MODEL = "embed-english-v3.0"
EMBEDDING_TRUNCATE = "END"

# Search configuration
SEARCH_TOP_K = 10
INCLUDE_DISTANCES = True

# Test configuration
TEST_CONFIGS = {
    'TECHNICAL_SKILLS': {
        'max_tokens': 100,
        'temperature': 0.6
    },
    'PROJECT_SELECTION': {
        'max_tokens': 90,
        'temperature': 0.7
    },
    'LEARNING_PATH': {
        'max_tokens': 120,
        'temperature': 0.5
    }
}