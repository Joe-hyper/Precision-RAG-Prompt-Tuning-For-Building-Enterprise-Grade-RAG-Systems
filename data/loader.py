# scripts/loader.py
import os

def load_text_files(data_dir):
    """
    Load text files from the specified directory.

    Args:
    - data_dir (str): The directory containing the text files.

    Returns:
    - texts (list): A list of strings, each representing the content of a text file.
    """
    texts = []
    for filename in os.listdir(data_dir):
        if filename.endswith('.txt'):
            with open(os.path.join(data_dir, filename), 'r') as file:
                texts.append(file.read())
    return texts

if __name__ == "__main__":
    raw_data_dir = '../data/data.txt'
    texts = load_text_files(raw_data_dir)
    for i, text in enumerate(texts):
        print(f"--- Text {i+1} ---")
        print(text)
        print()
