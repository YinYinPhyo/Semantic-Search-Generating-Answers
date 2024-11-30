from typing import List, Union, Optional
import textwrap

class DisplayFormatter:
    """Utility class for formatting and displaying test results"""
    
    def __init__(self, width: int = 80):
        self.width = width
        
    def format_header(self, text: str, level: int = 1) -> str:
        """Format section headers with different levels"""
        if level == 1:
            separator = "=" * self.width
            return f"\n{separator}\n{text}\n{separator}\n"
        elif level == 2:
            separator = "-" * self.width
            return f"\n{separator}\n{text}\n{separator}\n"
        else:
            return f"\n{text}\n{'-' * len(text)}\n"
    
    def format_test_case(self, number: int, description: str, question: str) -> str:
        """Format test case information"""
        return self.format_header(
            f"Test Case {number}: {description}", 
            level=2
        ) + f"Question: {question}\n"
    
    def format_generation(self, generation: any, 
                         index: Optional[int] = None, 
                         total: Optional[int] = None) -> str:
        """Format a single generation result"""
        # Handle Cohere Generation object or string
        # Use duck typing instead of explicit type checking
        text = getattr(generation, 'text', None)
        if text is None:
            text = str(generation)
        
        wrapped_text = textwrap.fill(text, width=self.width)
        if index is not None and total is not None:
            header = f"Generation {index + 1}/{total}:"
            return f"\n{header}\n{wrapped_text}\n"
        return wrapped_text
    
    def format_results(self, results: List[any], 
                      show_multiple: bool = True) -> str:
        """Format multiple generation results"""
        if not show_multiple:
            return self.format_generation(results[0])
            
        formatted_results = []
        for i, result in enumerate(results):
            formatted_results.append(
                self.format_generation(result, i, len(results))
            )
        return "\n".join(formatted_results)
    
    def display_test_results(self, test_cases: List[dict]) -> None:
        """Display all test cases and their results"""
        print(self.format_header("Test Results", level=1))
        
        for case in test_cases:
            print(self.format_test_case(
                case['number'],
                case['description'],
                case['question']
            ))
            print(self.format_results(
                case['results'],
                show_multiple=case.get('show_multiple', True)
            ))
            print("\n" + "-" * self.width) 