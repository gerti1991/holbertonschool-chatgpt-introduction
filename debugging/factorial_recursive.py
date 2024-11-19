#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    try:
        f = factorial(int(sys.argv[1]))
        print(f)
    except (IndexError, ValueError):
        print("Usage: ./factorial_recursive.py <non-negative integer>")
