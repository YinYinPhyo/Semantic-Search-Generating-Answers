class QuestionAnswerer:
    def __init__(self, cohere_client, search_engine):
        self.co = cohere_client
        self.search_engine = search_engine
        
    def generate_answer(self, question, num_generations=1, max_tokens=70,
                       model="command-nightly", temperature=0.5):
        """Generate answer for the given question"""
        results = self.search_engine.search(question)
        context = results[0]
        
        prompt = f"""
        Excerpt from the article titled "How to Build a Career in AI" by Andrew Ng: 
        {context}
        Question: {question}
        
        Extract the answer of the question from the text provided. 
        If the text doesn't contain the answer, reply that the answer is not available."""

        prediction = self.co.generate(
            prompt=prompt,
            max_tokens=max_tokens,
            model=model,
            temperature=temperature,
            num_generations=num_generations
        )
        
        return prediction.generations 