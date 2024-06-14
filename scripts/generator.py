# generator.py
import os
import openai
import numpy as np
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
from transformers import AutoTokenizer, AutoModel

# Load the API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def load_fabric_prompts():
    """
    Load the collection of prompts from danielmiessler/fabric.
    (For simplicity, we'll mock this function with some example prompts.)
    
    Returns:
    List[str]: A list of prompts.
    """
    prompts = [
        "What are the main benefits of using AI in healthcare?",
        "How can AI improve customer service?",
        "Explain the impact of AI on education.",
        # Add more prompts as needed
    ]
    return prompts

def embed_texts(texts, model_name="sentence-transformers/all-MiniLM-L6-v2"):
    """
    Embed a list of texts using a pre-trained transformer model.

    Parameters:
    texts (List[str]): List of texts to embed.
    model_name (str): The name of the model to use.

    Returns:
    np.ndarray: Embeddings for the texts.
    """
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)
    inputs = tokenizer(texts, return_tensors="pt", padding=True, truncation=True)
    outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1).detach().numpy()
    return embeddings

def generate_prompts(description, scenarios, model_name="sentence-transformers/all-MiniLM-L6-v2"):
    """
    Generate multiple prompt options based on the provided description and scenarios.

    Parameters:
    description (str): The user's description of their objective or task.
    scenarios (List[str]): A list of scenarios with expected outputs.

    Returns:
    List[str]: A list of generated prompts.
    """
    base_prompts = load_fabric_prompts()
    all_texts = [description] + scenarios + base_prompts
    embeddings = embed_texts(all_texts, model_name)

    # Calculate similarities
    description_embedding = embeddings[0].reshape(1, -1)
    similarities = cosine_similarity(description_embedding, embeddings[1:])

    # Rank and select top prompts
    top_indices = similarities[0].argsort()[-5:][::-1]  # Top 5 prompts
    generated_prompts = [base_prompts[i] for i in top_indices]
    
    return generated_prompts

# Example usage
if __name__ == "__main__":
    description = "Improve customer service using AI"
    scenarios = ["Reduce response time", "Increase customer satisfaction"]
    prompts = generate_prompts(description, scenarios)
    for prompt in prompts:
        print(prompt)
