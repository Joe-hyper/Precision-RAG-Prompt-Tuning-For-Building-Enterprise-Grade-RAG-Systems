# scripts/prompt_generator.py
import openai
from scripts.semantic_search import find_similar_prompts

def generate_prompt(prompt_template, variables):
    """
    Generate a prompt based on a template and variables.

    Args:
    - prompt_template (str): The prompt template.
    - variables (dict): Variables to fill into the template.

    Returns:
    - prompt (str): Generated prompt.
    """
    return prompt_template.format(**variables)

def get_openai_response(prompt):
    """
    Get a response from OpenAI's API based on the prompt.

    Args:
    - prompt (str): The prompt to send to the API.

    Returns:
    - response (str): Response from the API.
    """
    openai.api_key = 'your-api-key'
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

def generate_prompts(description, scenarios, corpus):
    """
    Generate multiple prompt options based on the description and scenarios.

    Args:
    - description (str): Description of the objective or task.
    - scenarios (list): List of scenarios with expected outputs.
    - corpus (list): Corpus of text for semantic search.

    Returns:
    - prompts (list): List of generated prompts.
    """
    prompts = []
    for scenario in scenarios:
        prompt = generate_prompt(description, scenario)
        similar_prompts = find_similar_prompts(prompt, corpus)
        prompts.extend(similar_prompts)
    return prompts

if __name__ == "__main__":
    description = "Translate the following English text to {language}"
    scenarios = [{"language": "French"}, {"language": "Spanish"}]
    corpus = [
        "Translate the following English text to Spanish",
        "Summarize the following text",
        "Generate a question based on this text",
        "Translate the following text to French",
        "Convert this text to a different language"
    ]
    prompts = generate_prompts(description, scenarios, corpus)
    for i, prompt in enumerate(prompts):
        print(f"--- Generated Prompt {i+1} ---")
        print(prompt)
