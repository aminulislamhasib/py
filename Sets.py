# Create a set with unique numeric elements
omega_pool = {10, 20, 30, 40, 50}        # Initialize a set with integer values
print(omega_pool)

# Create an empty set using the set() constructor
void_box = set()                         # Correct way to create an empty set

# Add a new element to the set
omega_pool.add(60)                       # Adds 60 to the set
print(omega_pool)

# Attempt to add a duplicate element
omega_pool.add(50)                       # Duplicate value, set remains unchanged
print(omega_pool)

# Remove an element using remove()
omega_pool.remove(40)                    # Removes 40, raises error if not found
print(omega_pool)

# Remove an element using discard()
omega_pool.discard(100)                  # Tries to remove 100, does nothing if not found
print(omega_pool)

# Create another set for operations
theta_pool = {20, 30, 70, 80}            # Another set with some overlapping values

print(omega_pool)
print(theta_pool)

# Check if one set is a subset of another
print(theta_pool.issubset(omega_pool))   # Returns True if all elements are in omega_pool

# Check if one set is a superset of another
print(omega_pool.issuperset(theta_pool)) # Returns True if omega_pool contains all elements

# Check if sets have no elements in common
print(omega_pool.isdisjoint(theta_pool)) # Returns True if no common elements

# Perform union operation
print(omega_pool | theta_pool)           # Combines all unique elements from both sets

# Perform intersection operation
print(omega_pool & theta_pool)           # Elements common to both sets

# Perform difference operation
print(omega_pool - theta_pool)           # Elements in omega_pool but not in theta_pool
print(theta_pool - omega_pool)

# Perform symmetric difference operation
print(omega_pool ^ theta_pool)           # Elements in either set but not both
print(theta_pool ^ omega_pool)

# Update the set using compound difference assignment
omega_pool -= theta_pool                 # Removes common elements from omega_pool

# Print updated set
print(omega_pool)                        # Shows modified set after operation
print(theta_pool)

# Check membership of an element
print(20 in omega_pool)                  # Returns True if 20 exists in the set

# Clear all elements from the set
omega_pool.clear()                       # Removes all elements

# Print the empty set
print(omega_pool)                        # Displays an empty set
