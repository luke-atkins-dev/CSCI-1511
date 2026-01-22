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
    gratuities = [.15, 0.2]
    calculated_gratuities = []

    # for grat in gratuities:
    #     calculated_gratuities.append({
    #         # f-string
    #         "percent": f"{grat*100:.0f}%",
    #         "dollar_amount": currency_format(total * grat),
    #         "total": currency_format(total*(1+grat))
    #     })
    # for grat in calculated_gratuities:
    #     percent = grat.get('percent')
    #     dollar_amount = grat.get('dollar_amount')
    #     print(f'{percent} Tip: {dollar_amount:>19}')
    dollar_amount_strings = []
    total_amount_strings = []
    for grat in gratuities:
        percent = f"{grat*100:.0f}%"
        dollar_amount = currency_format(total * grat)
        total_str = currency_format(total*(1+grat))
        dollar_amount_strings.append(f'{percent} Tip: {dollar_amount:>19}')
        total_amount_strings.append(f'Total with {percent} Tip:{total_str:>9}')
    print('\n'.join(dollar_amount_strings))
    print(f"Total:  {currency_format(total):>20}")
    print('\n'.join(total_amount_strings))
    # for grat in calculated_gratuities:
    #     percent = grat.get('percent')
    #     total = grat.get('total')
    #     print(f'Total with {percent} Tip:{total:>9}')
    input("Calculate another total (y/n)?: ") == "y" and main()
    
if __name__ == "__main__":
    main()