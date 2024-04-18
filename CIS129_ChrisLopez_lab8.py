# Author: Chris Lopez
# Date: April 17th, 2024
# Title: Palindrome Tester
#  This program was made to use the is_palindrome function to test if different words are a palindrome with the help of a stack.

def is_palindrome(input_string):
    # Remove case sensitivity, spaces, and punctuation from the string
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())
    
    # Initialize an empty list to use as a stack
    stack = []
    
    # Push all characters of the cleaned string onto the stack
    for char in cleaned_string:
        stack.append(char)
    
    # Compare characters popped from the stack to the characters in the cleaned string
    for char in cleaned_string:
        if stack.pop() != char:
            return False  # The string is not a palindrome
    
    return True  # The string is a palindrome

# The function can be tested with any string to check if it's a palindrome.
# Example:
is_palindrome("A man, a plan, a canal, Panama!")  # Should return True
