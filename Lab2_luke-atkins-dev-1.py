"""
Name: Restaurant Tip Calculator
Author: Luke Atkins
Purpose: This program calculates a tip percentage based off the bill total entered by the user
Starter Code: No starter code used
Date: 1/21/2026
"""

def force_input_type(prompt: str, error: str, output_type: type):
    """General use function for forcing valid CLI input types"""
    assert type(output_type) == type, "output_type must be a type"
    assert type(error) == str, "error message must be a string"
    assert type(prompt) == str, "prompt must be a string"

    result = input(prompt)

    try:
        return output_type(result)
    except ValueError:
        print(error)
        
        return force_input_type(prompt, error, output_type)

def currency_format(amount: float):
    """Converts number to USD format"""
    # f-string
    return f'${amount:,.2f}'

def main():
    print("Suggested Tip Calculator")
    total = force_input_type("Enter bill total: ", "Please enter a valid number", float)
    print(f"Total:  {currency_format(total):>20}")
    print(f'15% Tip:{currency_format(total*0.15):>20}')
    print(f'20% Tip:{currency_format(total*0.15):>20}')
    input("Calculate another total (y/n)?: ") == "y" and main()
    
if __name__ == "__main__":
    main()