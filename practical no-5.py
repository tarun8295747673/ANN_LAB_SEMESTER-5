# McCulloch-Pitts Neuron Function
def mcculloch_pitts_neuron(inputs, weights, bias, threshold):
    # Calculate weighted sum
    weighted_sum = sum([inputs[i] * weights[i] for i in range(len(inputs))]) + bias
    # Determine the output based on the threshold
    output = 1 if weighted_sum >= threshold else 0
    return output

# XOR Truth Table Input Data
input_data = [[0, 0], [0, 1], [1, 0], [1, 1]]

# Define appropriate values for Weights, Bias & Threshold for XOR
weights = [1, 1]
bias = -1
threshold = 1

# Evaluate the XOR function for each input
for inputs in input_data:
    result = mcculloch_pitts_neuron(inputs, weights, bias, threshold)
    print(f"Input: {inputs}, Output: {result}")
