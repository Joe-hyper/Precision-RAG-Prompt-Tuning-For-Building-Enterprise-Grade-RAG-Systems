# scripts/test_generator.py
import random

def generate_test_cases(description, scenarios, num_cases=5):
    """
    Generate test cases based on the description and scenarios.

    Args:
    - description (str): Description of the objective or task.
    - scenarios (list): List of scenarios with expected outputs.
    - num_cases (int): Number of test cases to generate.

    Returns:
    - test_cases (list): List of generated test cases.
    """
    test_cases = []
    for _ in range(num_cases):
        scenario = random.choice(scenarios)
        test_case = {}
        test_case["description"] = description
        test_case["input"] = scenario["input"]
        test_case["expected_output"] = scenario["expected_output"]
        test_cases.append(test_case)
    return test_cases

if __name__ == "__main__":
    description = "Translate the following English text to French"
    scenarios = [
        {"input": "Hello, how are you?", "expected_output": "Bonjour, comment ça va ?"},
        {"input": "What is your name?", "expected_output": "Comment vous appelez-vous ?"}
    ]
    test_cases = generate_test_cases(description, scenarios)
    for i, test_case in enumerate(test_cases):
        print(f"--- Test Case {i+1} ---")
        print(f"Description: {test_case['description']}")
        print(f"Input: {test_case['input']}")
        print(f"Expected Output: {test_case['expected_output']}")
        print()
