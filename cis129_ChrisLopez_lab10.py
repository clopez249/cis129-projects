#
# Author: Chris Lopez
#  Date: May 1st, 2024
#  Description: This program was made to imput dollar amounts that will then be returned in a check protected format.
#

def check_protection(amount: float) -> str:
    """
    Formats a given amount into a check-protected format with leading asterisks,
    filling a fixed space of 10 characters.
    
    Parameters:
        amount (float): The dollar amount to format.
        
    Returns:
        str: The formatted amount with leading asterisks for check protection.
    """
    # Format the amount to have two decimal places
    formatted_amount = f"{amount:,.2f}"
    
    # Calculate the number of leading asterisks needed
    number_of_asterisks = 10 - len(formatted_amount)
    
    # Generate the protected check amount
    protected_amount = '*' * number_of_asterisks + formatted_amount
    
    return protected_amount

# Example usage
print(check_protection(399.87))
