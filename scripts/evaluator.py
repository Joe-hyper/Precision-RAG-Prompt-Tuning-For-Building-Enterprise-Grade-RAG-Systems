
# scripts/evaluator.py
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def evaluate_prompts_with_test_cases(prompts, test_cases):
    """
    Evaluate prompts using the provided test cases.

    Args:
    - prompts (list): List of generated prompts.
    - test_cases (list): List of test cases.

    Returns:
    - evaluations (dict): Dictionary containing evaluation scores for each prompt.
    """
    evaluations = {}
    for prompt in prompts:
        prompt_embedding = model.encode(prompt, convert_to_tensor=True)
        scores = []
        for test_case in test_cases:
            description_embedding = model.encode(test_case['description'], convert_to_tensor=True)
            input_embedding = model.encode(test_case['input'], convert_to_tensor=True)
            expected_output_embedding = model.encode(test_case['expected_output'], convert_to_tensor=True)
            input_score = cosine_similarity(prompt_embedding, input_embedding)
            expected_output_score = cosine_similarity(prompt_embedding, expected_output_embedding)
            description_score = cosine_similarity(prompt_embedding, description_embedding)
            total_score = input_score + expected_output_score + description_score
            scores.append(total_score)
        evaluations[prompt] = sum(scores) / len(scores)
    return evaluations

if __name__ == "__main__":
    prompts = [
        "Translate the following English text to French",
        "Summarize the following text",
        "Generate a question based on this text",
        "Translate the following text to Spanish",
        "Convert this text to a different language"
    ]
    test_cases = [
        {"description": "Translate the following English text to French", "input": "Hello, how are you?", "expected_output": "Bonjour, comment ça va ?"},
        {"description": "Translate the following English text to French", "input": "What is your name?", "expected_output": "Comment vous appelez-vous ?"}
    ]
    evaluations = evaluate_prompts_with_test_cases(prompts, test_cases)
    for prompt, score in evaluations.items():
        print(f"--- Prompt ---")
        print(f"Prompt: {prompt}")
        print(f"Evaluation Score: {score}")
        print()
