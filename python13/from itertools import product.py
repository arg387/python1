from itertools import product

# Define the CNOT gate function
#len() function give us length of inputs
#def is used to make new function and store codes within them
# max() function used to return the item with highest value
def cnot_gate(input_bits):
    if len(input_bits) != 2:
        raise ValueError("CNOT gate requires 2 input bits")
    # Apply CNOT gate logic
    output_bits = [input_bits[0], input_bits[0] ^ input_bits[1]]
    return output_bits

# Create an empty ArrayList to store results
results = []

# Generate all possible input combinations
input_combinations = list(product([0, 1], repeat=2))

# Verify the truth table and store results in the ArrayList
for inputs in input_combinations:
    input_bits = list(inputs)
    output_bits = cnot_gate(input_bits)
    results.append((input_bits, output_bits))

