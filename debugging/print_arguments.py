#!/usr/bin/python3
import sys

# Check if any arguments were passed
if len(sys.argv) == 1:
    print("No arguments were passed.")
else:
    # Iterate through the arguments (excluding the script name)
    for arg in sys.argv[1:]:
        print(arg)
