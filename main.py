import numpy as np
import matplotlib.pyplot as plt

def generate_rule(rule_number):
    rule_string = format(rule_number, "08b")
    return {format(i, "03b"): rule_string[::-1][i] for i in range(8)}

def apply_rule(rule, cells):
    return [rule[cells[i-1:i+2]] for i in range(1, len(cells) - 1)]

def run_automata(rule_number, initial_state, num_steps):
    rule = generate_rule(rule_number)
    current_state = initial_state
    history = [current_state]

    for _ in range(num_steps):
        current_state = "0" + "".join(apply_rule(rule, current_state)) + "0"
        history.append(current_state)
    
    return history

def plot_automata(history):
    cells = np.array([[int(cell) for cell in row] for row in history])
    plt.imshow(cells, cmap="binary", interpolation="nearest")
    plt.show()

if __name__ == "__main__":
    rule_number = 30
    initial_state = "0000000001000000000"
    num_steps = 15
