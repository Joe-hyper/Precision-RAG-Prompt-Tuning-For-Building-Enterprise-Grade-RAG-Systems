# main.py
from loader import load_data
from generator import generate_prompts
from evaluation_data_generator import generate_evaluation_data
from evaluation import evaluate_prompts

def main():
    data_path = r"C:\Users\Jojo\Desktop\10A\10x\Week7\Precision-RAG-Prompt-Tuning-For-Building-Enterprise-Grade-RAG-Systems\data\prompts.txt"
    data = load_data(data_path)
    print("Data Loaded")

    description = "Improve customer service using AI"
    scenarios = ["Reduce response time", "Increase customer satisfaction"]
    prompts = generate_prompts(description, scenarios)
    print("Generated Prompts:")
    for prompt in prompts:
        print(prompt)
    
    evaluation_data = generate_evaluation_data(description, scenarios)
    print("\nGenerated Evaluation Data:")
    print(evaluation_data.head())
    
    evaluation_results = evaluate_prompts(description, prompts, evaluation_data)
    print("\nEvaluation Results:")
    print(evaluation_results.head())

if __name__ == "__main__":
    main()
