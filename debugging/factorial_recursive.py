#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if len(sys.argv) != 2:
    print("Usage: python3 factorial.py <positive integer>")
    sys.exit(1)

try:
    number = int(sys.argv[1])
    if number < 0:
        print("Error: Please enter a positive integer.")
        sys.exit(1)
except ValueError:
    print("Error: Input must be an integer.")
    sys.exit(1)

f = factorial(number)
print(f)
