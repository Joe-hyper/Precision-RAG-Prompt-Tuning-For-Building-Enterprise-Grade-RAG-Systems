# scripts/design_ui.py
from tkinter import *

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
generate_button = Button(root, text="Generate Prompts", padx=20, pady=10)
generate_button.pack()

# Create a text area to display generated prompts
prompt_text = Text(root, height=10, width=50)
prompt_text.pack()

# Create a button to evaluate prompts
evaluate_button = Button(root, text="Evaluate Prompts", padx=20, pady=10)
evaluate_button.pack()

# Create a text area to display evaluation results
evaluation_text = Text(root, height=10, width=50)
evaluation_text.pack()

# Run the main event loop
root.mainloop()
