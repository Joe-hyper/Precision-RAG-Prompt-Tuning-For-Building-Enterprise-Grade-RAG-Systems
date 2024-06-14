# evaluation.py
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from transformers import AutoTokenizer, AutoModel

def evaluate_prompts(description, prompts, evaluation_data, model_name="sentence-transformers/all-MiniLM-L6-v2"):
    """
    Evaluate generated prompts based on their alignment with the evaluation data.

    Parameters:
    description (str): The user's description of their objective or task.
    prompts (List[str]): A list of generated prompts.
    evaluation_data (pd.DataFrame): The evaluation data containing scenarios.

    Returns:
    pd.DataFrame: The evaluation results as a DataFrame.
    """
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)
    
    all_texts = [description] + prompts + list(evaluation_data["scenario"])
    embeddings = embed_texts(all_texts, model_name)
    
    description_embedding = embeddings[0].reshape(1, -1)
    prompt_embeddings = embeddings[1:len(prompts)+1]
    scenario_embeddings = embeddings[len(prompts)+1:]
    
    alignment_scores = cosine_similarity(prompt_embeddings, scenario_embeddings)
    
    evaluation_results = []
    for i, prompt in enumerate(prompts):
        scores = alignment_scores[i]
        scenario_scores = list(zip(list(evaluation_data["scenario"]), scores))
        evaluation_results.append({"prompt": prompt, "scenario_scores": scenario_scores})
    
    return pd.DataFrame(evaluation_results)

# Example usage
if __name__ == "__main__":
    description = "Improve customer service using AI"
    prompts = [
        "How can AI improve customer service?",
        "What are the main benefits of using AI in healthcare?",
        "Explain the impact of AI on education."
    ]
    evaluation_data = pd.DataFrame({
        "scenario": ["Reduce response time", "Increase customer satisfaction"]
    })
    evaluation_results = evaluate_prompts(description, prompts, evaluation_data)
    print(evaluation_results.head())
