#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
def get_user_input():
    """Validate and return a positive integer from the user."""
    while True:
        try:
            n = int(input("Enter how many terms of the Fibonacci sequence you want: "))
            if n > 0:
                return n
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def generate_fibonacci(n):
    """Generate a Fibonacci sequence up to n terms and return as a list."""
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def print_fibonacci(sequence):
    """Print the Fibonacci sequence in a readable format."""
    print("Fibonacci sequence:")
    print(", ".join(map(str, sequence)))

def main():
    num_terms = get_user_input()
    sequence = generate_fibonacci(num_terms)
    print_fibonacci(sequence)

if __name__ == "__main__":
    main()
