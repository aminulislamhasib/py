# =========================
# PYTHON MODULES & IMPORTS
# =========================

# A module is a file that contains reusable code (functions, classes, variables)
# Python provides many built-in modules like math, random, datetime, re, etc.

# -------------------------
# BASIC IMPORT
# -------------------------

import math                             # Import the entire math module

print(math.sqrt(49))                    # Call sqrt() using dot notation (module.function)
print(math.pi)                          # Access a constant from the module


# -------------------------
# IMPORT WITH ALIAS
# -------------------------

import math as mx                       # Import module with a shorter alias

print(mx.sqrt(64))                      # Use alias instead of full module name


# -------------------------
# IMPORT SPECIFIC ELEMENTS
# -------------------------

from math import sin, cos, radians      # Import only selected functions

angle_deg = 30                          # Store angle in degrees
angle_rad = radians(angle_deg)          # Convert degrees to radians

print(sin(angle_rad))                   # Call sin() directly (no module prefix)
print(cos(angle_rad))                   # Call cos() directly


# -------------------------
# IMPORT WITH ALIAS (SPECIFIC)
# -------------------------

from math import sqrt as sq             # Import sqrt with alias

print(sq(81))                           # Use alias instead of original name


# -------------------------
# IMPORT EVERYTHING (NOT RECOMMENDED)
# -------------------------

from math import *                      # Import all functions (can cause conflicts)

print(sqrt(25))                         # Direct use without module prefix
print(pow(2, 3))                        # Another function from math


# -------------------------
# USING ANOTHER MODULE (datetime)
# -------------------------

import datetime                         # Import datetime module

dt_obj = datetime.date(2000, 1, 1)      # Create a date object (year, month, day)

print(dt_obj.day)                       # Access day attribute
print(dt_obj.month)                     # Access month attribute
print(dt_obj.year)                      # Access year attribute


# -------------------------
# MAIN CHECK IDIOM
# -------------------------

# This condition checks whether the file is run directly or imported
if __name__ == '__main__':              # True only when script is executed directly
    print("Running as main program")    # This code runs only in direct execution


# -------------------------
# NOTES (IMPORTANT IDEAS)
# -------------------------

# - Modules = reusable code files (like toolboxes)
# - import module → access with module.name
# - import module as alias → shorter name
# - from module import name → use directly
# - from module import * → avoid (name conflicts)
# - __name__ == '__main__' → controls execution behavior
