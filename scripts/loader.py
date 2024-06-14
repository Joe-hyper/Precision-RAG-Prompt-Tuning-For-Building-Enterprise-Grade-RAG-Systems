# loader.py
import os
import pandas as pd

def load_data(file_path):
    """
    Load data from a text file.

    Parameters:
    file_path (str): The path to the text file.

    Returns:
    pd.DataFrame: The loaded data as a DataFrame.
    """
    if os.path.exists(file_path):
        data = pd.read_csv(file_path, delimiter='\t')  # Assuming tab-delimited file
        return data
    else:
        raise FileNotFoundError(f"File at {file_path} not found.")

# Example usage
if __name__ == "__main__":
    data_path = r"C:\Users\Jojo\Desktop\10A\10x\Week7\Precision-RAG-Prompt-Tuning-For-Building-Enterprise-Grade-RAG-Systems\data\prompts.txt"
    data = load_data(data_path)
    print(data.head())
