# Week 2, Day 4: Modules, Packages, Virtual Environments

## Part 1: Modules
# A module is just a .py file you can import and reuse elsewhere.

# --- helpers.py ---
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

PI_APPROX = 3.14


# --- day4-modules.py ---
import helpers

print(helpers.greet("Tuan"))
print(helpers.add(3, 5))
print(helpers.PI_APPROX)

# You can also import specific things directly, skipping the prefix:
from helpers import greet, add

print(greet("Tuan"))
print(add(3, 5))


## Part 2: Packages
# A package is a FOLDER of modules with an __init__.py file inside
# (can be empty) that tells Python to treat the folder as importable.
#
# my_package/
# ├── __init__.py
# ├── math_utils.py
# └── string_utils.py
#
# Used to organize related modules together as a project grows.


## Part 3: Virtual Environments
# An isolated Python setup per project, so one project's packages don't
# conflict with another's.

# Create one:
#   python3 -m venv venv
#
# (If it fails with "ensurepip is not available" on WSL/Ubuntu, first run:
#   sudo apt install python3.12-venv
#  then retry python3 -m venv venv)

# Activate it:
#   source venv/bin/activate
# -> (venv) appears at the start of the terminal prompt when active

# Install a package while active:
#   pip install requests

# Deactivate when done:
#   deactivate


## .gitignore
# Prevents the large, machine-specific venv/ folder from being committed.
#
# --- .gitignore ---
# venv/