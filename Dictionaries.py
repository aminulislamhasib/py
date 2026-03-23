# Create a dictionary with different key-value pairs
alpha_map = {
    'x1': 'Item Alpha',              # Key 'x1' stores a string value
    'y2': 12.5,                      # Key 'y2' stores a float value
    'z3': 999,                       # Key 'z3' stores an integer value
    'w4': ['a', 'b']                 # Key 'w4' stores a list
}

# Create another dictionary using the dict() constructor with tuples
beta_map = dict([
    ('p9', 'Item Alpha'),            # Tuple with key 'p9' and string value
    ('q8', 12.5),                    # Tuple with key 'q8' and float value
    ('r7', 999),                     # Tuple with key 'r7' and integer value
    ('s6', ['a', 'b'])               # Tuple with key 's6' and list value
])

# Access a value using a key from the dictionary
print(alpha_map['x1'])               # Prints the value associated with key 'x1'

# Update the value of an existing key
alpha_map['x1'] = 'Item Beta'        # Changes the value of key 'x1'
# Print the updated value
print(alpha_map['x1'])               # Displays the updated value

# Safely retrieve a value using .get() with a default fallback
print(alpha_map.get('w4', []))       # Returns value of 'w4' or empty list if not found

# Retrieve all keys from the dictionary
print(alpha_map.keys())              # Displays all keys in the dictionary
# Retrieve all values from the dictionary
print(alpha_map.values())            # Displays all values in the dictionary

# Retrieve all key-value pairs as tuples
print(alpha_map.items())             # Displays all key-value pairs

# Remove a key-value pair and return its value (with default if missing)
print(alpha_map.pop('y2', 0))        # Removes 'y2' and returns its value or 0
# Remove the last inserted key-value pair
print(alpha_map.popitem())           # Removes and returns the last item

# Update dictionary with new key-value pairs
alpha_map.update({
    'y2': 20,                        # Adds or updates key 'y2'
    'n5': 50                         # Adds a new key 'n5'
})
# Print the updated dictionary
print(alpha_map)                     # Displays the modified dictionary

# Clear all elements from the dictionary
alpha_map.clear()                   # Removes all key-value pairs
# Print the empty dictionary
print(alpha_map)                     # Displays an empty dictionary