import tkinter as tk

# Define the rules
def rule1(attacks):
    if 'thunder' in attacks and 'swift' in attacks and 'thunderbolt' in attacks:
        return 'You may have a pikachu.'
    return None

def rule2(attacks):
    if 'fireblast' in attacks and 'pound' in attacks and 'bite' in attacks:
        return 'You may have a charizard.'
    return None

def rule3(attacks):
    if 'hydropump' in attacks and 'watergun' in attacks and 'tackle' in attacks:
        return 'You may have a Blastoise.'
    return None

def rule4(attacks):
    if 'Solarbeam' in attacks and 'leechseed' in attacks and 'vinegrips' in attacks:
        return 'You may have Venusaur.'
    return None

def rule5(attacks):
    if 'icebeam' in attacks and 'dragonclaw' in attacks and 'thundershock' in attacks:
        return 'You may have a Dragonite.'
    return None

# Define the expert system
def diagnose(attacks):
    rules = [rule1, rule2, rule3, rule4, rule5]
    results = []
    for rule in rules:
        result = rule(attacks)
        if result:
            results.append(result)
    if len(results) == 0:
        return 'Sorry, we could not identify your pokemon.'
    elif len(results) == 1:
        return results[0]
    else:
        return 'You may have multiple pokemons: ' + ', '.join(results)

def get_diagnosis():
    input_attacks = entry.get()
    attacks = input_attacks.lower().split()
    result = diagnose(attacks)
    diagnosis_label.config(text=result)

# Create the GUI
root = tk.Tk()
root.title("Pokemon Guess")
root.geometry("400x200")

# Create input field
entry = tk.Entry(root, width=40)
entry.pack(pady=20)

# Create diagnosis button
diagnose_button = tk.Button(root, text="Guess my pokemon", command=get_diagnosis)
diagnose_button.pack()

# Create label for diagnosis result
diagnosis_label = tk.Label(root, text="")
diagnosis_label.pack(pady=20)

root.mainloop()