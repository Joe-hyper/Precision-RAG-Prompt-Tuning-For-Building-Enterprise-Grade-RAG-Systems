# evaluation_data_generator.py
import pandas as pd

def generate_evaluation_data(description, scenarios):
    """
    Generate evaluation data based on the user's description and scenarios.

    Parameters:
    description (str): The user's description of their objective or task.
    scenarios (List[str]): A list of scenarios with expected outputs.

    Returns:
    pd.DataFrame: The generated evaluation data as a DataFrame.
    """
    evaluation_data = []
    for scenario in scenarios:
        evaluation_data.append({"description": description, "scenario": scenario})
    
    return pd.DataFrame(evaluation_data)

# Example usage
if __name__ == "__main__":
    description = "Improve customer service using AI"
    scenarios = ["Reduce response time", "Increase customer satisfaction"]
    evaluation_data = generate_evaluation_data(description, scenarios)
    print(evaluation_data.head())
