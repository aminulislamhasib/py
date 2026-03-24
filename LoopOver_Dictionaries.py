# Create a dictionary with random keys and numeric values
gamma_box = {
    'aX': 1200,                     # Key 'aX' stores an integer value
    'bY': 450,                      # Key 'bY' stores an integer value
    'cZ': 300,                      # Key 'cZ' stores an integer value
    'dW': 150                       # Key 'dW' stores an integer value
}

# Loop through all values in the dictionary and print each one
for val in gamma_box.values():      # Iterate over all values in the dictionary
    print(val)                      # Print each value

# Loop through all keys in the dictionary and print each one
for key in gamma_box:               # Iterate over all keys (default behavior)
    print(key)                      # Print each key
for key in gamma_box.keys():        # Iterate over all keys 
    print(key)                      # Print each key


# Loop through all key-value pairs and print them as tuples
for pair in gamma_box.items():      # Iterate over key-value pairs as tuples
    print(pair)                     # Print each tuple (key, value)

# Loop through key-value pairs and unpack them into separate variables
for k, v in gamma_box.items():      # Unpack key into k and value into v
    print(k, v)                     # Print key and value separately

# Apply a transformation to each value and update the dictionary
for k, v in gamma_box.items():      # Iterate over key-value pairs
    gamma_box[k] = round(v * 0.75)  # Modify each value by multiplying and rounding
# Print the updated dictionary
print(gamma_box)                    # Display dictionary after modification

# Use enumerate to loop through keys with an index
for idx, key in enumerate(gamma_box):  # idx is the counter, key is the dictionary key
    print(idx, key)                    # Print index and key
# Use enumerate to loop through values with an index
for idx, val in enumerate(gamma_box.values()):  # idx is the counter, val is the value
    print(idx, val)                            # Print index and value

# Use enumerate with items to get index and key-value pairs
for idx, pair in enumerate(gamma_box.items()):  # idx is counter, pair is (key, value)
    print(idx, pair)                            # Print index and tuple

# Use enumerate with a custom starting index
for idx, pair in enumerate(gamma_box.items(), 5):  # Start counting from 5
    print(idx, pair)                               # Print index and tuple
