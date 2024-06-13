# scripts/elo_rating.py
import math

def expected_result(rating1, rating2):
    """
    Calculate the expected result between two prompts based on their ratings.

    Args:
    - rating1 (float): Rating of prompt 1.
    - rating2 (float): Rating of prompt 2.

    Returns:
    - expected_result (float): Expected result for prompt 1.
    """
    return 1 / (1 + math.pow(10, (rating2 - rating1) / 400))

def update_ratings(rating1, rating2, score, k=32):
    """
    Update the ELO ratings based on the result of a match.

    Args:
    - rating1 (float): Rating of prompt 1.
    - rating2 (float): Rating of prompt 2.
    - score (int): Score of the match (0 or 1, indicating which prompt won).
    - k (float): Weight constant.

    Returns:
    - new_rating1 (float): Updated rating for prompt 1.
    - new_rating2 (float): Updated rating for prompt 2.
    """
    expected = expected_result(rating1, rating2)
    if score == 1:
        actual = 1
    else:
        actual = 0
    new_rating1 = rating1 + k * (actual - expected)
    new_rating2 = rating2 + k * (expected - actual)
    return new_rating1, new_rating2

if __name__ == "__main__":
    prompt1_rating = 1000
    prompt2_rating = 1200
    score = 1
    new_prompt1_rating, new_prompt2_rating = update_ratings(prompt1_rating, prompt2_rating, score)
    print(f"New Rating for Prompt 1: {new_prompt1_rating}")
    print(f"New Rating for Prompt 2: {new_prompt2_rating}")
