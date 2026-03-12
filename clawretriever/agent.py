from openclaw import Agent, Message
from typing import Optional

class RetrievalAgent:
    """OpenClaw agent specialized in answering queries based on retrieved context."""
    
    def __init__(self, model_name: str = "gpt-3.5-turbo"):
        self.agent = Agent(
            name="KnowledgeBot",
            instructions="You are a helpful assistant. Use the provided context to answer questions accurately."
        )

    def generate_response(self, query: str, context: str) -> str:
        prompt = f"""
        Use the context below to answer the user query. If the answer is not in the context, 
        state that you don't know based on the provided documents.
        
        Context:
        {context}
        
        User Query: {query}
        """
        
        message = Message(role="user", content=prompt)
        # Assuming openclaw's interface for completion
        response = self.agent.run(message)
        return response.content
