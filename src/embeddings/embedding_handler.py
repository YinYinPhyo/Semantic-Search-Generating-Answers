import cohere
import numpy as np
from annoy import AnnoyIndex

class EmbeddingHandler:
    def __init__(self, api_key):
        self.co = cohere.Client(api_key)
        
    def get_embeddings(self, texts):
        """Get embeddings for the given texts"""
        return self.co.embed(texts=texts.tolist()).embeddings
        
    def build_search_index(self, embeddings, num_trees, filename):
        """Build and save search index"""
        embeds = np.array(embeddings)
        search_index = AnnoyIndex(embeds.shape[1], 'angular')
        
        for i in range(len(embeds)):
            search_index.add_item(i, embeds[i])
            
        search_index.build(num_trees)
        search_index.save(filename)
        return search_index 