# scripts/implement_ui.py
from tkinter import *
from tkinter import messagebox
import scripts.prompt_generation as pg
import scripts.evaluator as ev

def generate_prompts():
    description = description_entry.get()
    scenarios = scenarios_entry.get().split(",")
    prompts = pg.generate_prompts(description, scenarios)
    prompt_text.delete(1.0, END)
    for prompt in prompts:
        prompt_text.insert(END, prompt + "\n")

def evaluate_prompts():
    prompts = prompt_text.get(1.0, END).split("\n")
    test_cases = ev.generate_test_cases(description_entry.get(), scenarios_entry.get())
    evaluations = ev.evaluate_prompts_with_test_cases(prompts, test_cases)
    evaluation_text.delete(1.0, END)
    for prompt, score in evaluations.items():
        evaluation_text.insert(END, f"Prompt: {prompt}, Score: {score}\n")

# Create the main window
root = Tk()
root.title("Prompt Engineering System")

# Create labels and entry fields for user input
description_label = Label(root, text="Description:")
description_label.pack()
description_entry = Entry(root, width=50)
description_entry.pack()

scenarios_label = Label(root, text="Scenarios (separated by commas):")
scenarios_label.pack()
scenarios_entry = Entry(root, width=50)
scenarios_entry.pack()

# Create a button to generate prompts
generate_button = Button(root, text="Generate Prompts", padx=20, pady=10, command=generate_prompts)
generate_button.pack()

# Create a text area to display generated prompts
prompt_text = Text(root, height=10, width=50)
prompt_text.pack()

# Create a button to evaluate prompts
evaluate_button = Button(root, text="Evaluate Prompts", padx=20, pady=10, command=evaluate_prompts)
evaluate_button.pack()

# Create a text area to display evaluation results
evaluation_text = Text(root, height=10, width=50)
evaluation_text.pack()

# Run the main event loop
root.mainloop()
