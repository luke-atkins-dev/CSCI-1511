
"""
Purpose: This program uses a user's static name and will print the lower, upper, and title case version centered with underscores
Author: Luke Atkins
Starter Code: No starter code used
Date: 1/20/2026
"""

def main(name):
    print_name = lambda func: print(f'{func(name):_^20}')

    print_name(str.lower)
    print_name(str.upper)
    print_name(str.title) # Not necessary

if __name__ == "__main__":
    user_name = "Luke Atkins"
    main(user_name)