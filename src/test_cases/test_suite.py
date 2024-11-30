from typing import Dict, List
from dataclasses import dataclass
import sys
import os

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from config.config import (
    DEFAULT_NUM_GENERATIONS,
    MAX_TOKENS,
    TEMPERATURE,
    MODEL_NAME,
    TEST_CONFIGS
)

@dataclass
class TestCase:
    number: int
    description: str
    question: str
    show_multiple: bool = True
    num_generations: int = DEFAULT_NUM_GENERATIONS
    max_tokens: int = MAX_TOKENS
    temperature: float = TEMPERATURE
    model: str = MODEL_NAME

class TestSuite:
    def __init__(self, qa_system):
        self.qa_system = qa_system
        self.test_cases = self._initialize_test_cases()
    
    def _initialize_test_cases(self) -> List[Dict]:
        """Initialize all test cases"""
        test_cases = [
            # Original test cases
            TestCase(
                number=1,
                description="Single Generation - Side Projects",
                question="Are side projects important when you are starting to learn about AI?",
                show_multiple=False
            ),
            TestCase(
                number=2,
                description="Multiple Generations - Career Building",
                question="Are side projects a good idea when trying to build a career in AI?",
                num_generations=3
            ),
            TestCase(
                number=3,
                description="Out of Domain Question",
                question="What is the most viewed televised event?",
                num_generations=5
            ),
            # New test cases
            TestCase(
                number=4,
                description="Technical Skills Question",
                question="What are the most important technical skills for a career in AI?",
                num_generations=2,
                max_tokens=100
            ),
            TestCase(
                number=5,
                description="Project Selection",
                question="How should I choose which AI project to work on?",
                temperature=0.7
            ),
            TestCase(
                number=6,
                description="Learning Path",
                question="What's the recommended learning path for AI?",
                num_generations=3,
                max_tokens=120
            ),
            TestCase(
                number=7,
                description="Community Impact",
                question="How important is community in AI career development?",
                show_multiple=False
            ),
            TestCase(
                number=8,
                description="Job Search Specifics",
                question="How is searching for an AI job different from other fields?",
                num_generations=2
            )
        ]
        
        return [self._create_test_dict(case) for case in test_cases]
    
    def _create_test_dict(self, case: TestCase) -> Dict:
        """Convert TestCase to dictionary and generate results"""
        results = self.qa_system.generate_answer(
            question=case.question,
            num_generations=case.num_generations,
            max_tokens=case.max_tokens,
            model=case.model,
            temperature=case.temperature
        )
        
        return {
            'number': case.number,
            'description': case.description,
            'question': case.question,
            'show_multiple': case.show_multiple,
            'results': results
        }
    
    def run_all_tests(self, formatter) -> None:
        """Run all test cases and display results"""
        formatter.display_test_results(self.test_cases) 