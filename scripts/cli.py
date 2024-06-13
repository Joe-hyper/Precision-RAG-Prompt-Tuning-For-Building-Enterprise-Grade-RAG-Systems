# scripts/cli.py
import argparse
from scripts.loader import load_text_files
from scripts.prompt_generator.py import generate_prompts
from scripts.evaluator.py import evaluate_prompts

def main(description, scenarios):
    corpus = load_text_files('../data/data.txt')
    prompts = generate_prompts(description, scenarios, corpus)
    evaluations = evaluate_prompts(prompts, description)

    for i, (prompt, score) in enumerate(zip(prompts, evaluations)):
        print(f"--- Generated Prompt {i+1} ---")
        print(f"Prompt: {prompt}")
        print(f"Score: {score}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Prompt Generation System")
    parser.add_argument("--description", type=str, required=True, help="Description of the objective or task")
    parser.add_argument("--scenarios", type=str, nargs='+', required=True, help="Scenarios with expected outputs")
    args = parser.parse_args()
    
    scenarios = [eval(scenario) for scenario in args.scenarios]  # Convert string representation of dict to dict
    main(args.description, scenarios)
