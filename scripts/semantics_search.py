# scripts/semantic_search.py
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def find_similar_prompts(prompt, corpus, top_k=5):
    """
    Find semantically similar prompts from the corpus.

    Args:
    - prompt (str): The input prompt.
    - corpus (list): The corpus of text.
    - top_k (int): The number of similar prompts to return.

    Returns:
    - similar_prompts (list): List of similar prompts.
    """
    corpus_embeddings = model.encode(corpus, convert_to_tensor=True)
    query_embedding = model.encode(prompt, convert_to_tensor=True)
    hits = util.semantic_search(query_embedding, corpus_embeddings, top_k=top_k)
    similar_prompts = [corpus[hit['corpus_id']] for hit in hits[0]]
    return similar_prompts

if __name__ == "__main__":
    test_prompt = "Translate the following English text to French"
    corpus = [
        "Translate the following English text to Spanish",
        "Summarize the following text",
        "Generate a question based on this text",
        "Translate the following text to French",
        "Convert this text to a different language"
    ]
    similar_prompts = find_similar_prompts(test_prompt, corpus)
    for i, prompt in enumerate(similar_prompts):
        print(f"--- Similar Prompt {i+1} ---")
        print(prompt)
