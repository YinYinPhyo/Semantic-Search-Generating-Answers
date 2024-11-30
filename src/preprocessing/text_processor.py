import numpy as np

class TextProcessor:
    @staticmethod
    def process_text(text):
        """Split text into paragraphs and clean them"""
        # Split into paragraphs
        texts = text.split('\n\n')
        
        # Clean up paragraphs
        texts = np.array([t.strip(' \n') for t in texts if t])
        return texts 