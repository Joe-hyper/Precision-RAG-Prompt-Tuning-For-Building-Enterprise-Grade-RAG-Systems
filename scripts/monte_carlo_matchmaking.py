# scripts/monte_carlo_matchmaking.py
import random

def monte_carlo_matchmaking(prompts, num_matches=1000):
    """
    Perform Monte Carlo matchmaking to test prompt effectiveness.

    Args:
    - prompts (list): List of prompts to match against each other.
    - num_matches (int): Number of matches to simulate for each prompt.

    Returns:
    - match_results (dict): Dictionary containing match results for each prompt.
    """
    match_results = {prompt: 0 for prompt in prompts}
    for _ in range(num_matches):
        prompt1, prompt2 = random.sample(prompts, 2)
        # Simulate a "match" between prompt1 and prompt2
        winner = random.choice([prompt1, prompt2])
        match_results[winner] += 1
    return match_results

if __name__ == "__main__":
    prompts = [
        "Translate the following English text to French",
        "Summarize the following text",
        "Generate a question based on this text",
        "Translate the following text to Spanish",
        "Convert this text to a different language"
    ]
    match_results = monte_carlo_matchmaking(prompts)
    for prompt, wins in match_results.items():
        print(f"Prompt: {prompt}")
        print(f"Wins: {wins}")
        print()
