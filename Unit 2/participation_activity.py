
"""
Purpose: This program uses a user's static name and will print the lower, upper, and title case version centered with padding
Author: Luke Atkins
Starter Code: No starter code used
Date: 1/20/2026
"""

def main(name):
    padding = " " * 5
    print_name = lambda func: print(f'{padding}{func(name)}{padding}')

    print_name(str.lower)
    print_name(str.upper)
    print_name(str.title) # Not necessary

if __name__ == "__main__":
    user_name = "Luke Atkins"
    main(user_name)