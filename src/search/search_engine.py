#################################################
# Step 3: Searching Articles
#################################################

class SearchEngine:
    def __init__(self, cohere_client, search_index, texts):
        """Initialize search engine with required components"""
        self.co = cohere_client
        self.search_index = search_index
        self.texts = texts
        
    def search(self, query, num_neighbors=10):
        """
        Search for relevant texts given a query
        
        Args:
            query (str): The search query
            num_neighbors (int): Number of nearest neighbors to retrieve
            
        Returns:
            numpy.ndarray: Array of relevant text passages
        """
        query_embed = self.co.embed(texts=[query]).embeddings
        similar_item_ids = self.search_index.get_nns_by_vector(
            query_embed[0],
            num_neighbors,
            include_distances=True
        )
        return self.texts[similar_item_ids[0]] 