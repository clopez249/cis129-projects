# Author: Chris Lopez
# Lab 3 of my CIS 129 Course
# Coffee Shop Simulator

# Function to calculate total cost with tax
def calculate_total(coffee_count, muffin_count, croissant_count, pastry_count):
    coffee_price = 5
    muffin_price = 4
    croissant_price = 6
    pastry_price = 3
    tax_rate = 0.06
    
    coffee_cost = coffee_count * coffee_price
    muffin_cost = muffin_count * muffin_price
    croissant_cost = croissant_count * croissant_price
    pastry_cost = pastry_count * pastry_price
    
    subtotal = coffee_cost + muffin_cost + croissant_cost + pastry_cost
    tax = subtotal * tax_rate
    total = subtotal + tax
    
    return total, subtotal, tax

# Function to display the receipt
def display_receipt(coffee_count, muffin_count, croissant_count, pastry_count, total, subtotal, tax):
    print("***************************************")
    print("Chris' Famous Coffee")
    print(f"{coffee_count} Coffee at $5 each: ${coffee_count * 5:.2f}")
    print(f"{muffin_count} Muffins at $4 each: ${muffin_count * 4:.2f}")
    print(f"{croissant_count} Croissants at $6 each: ${croissant_count * 6:.2f}")
    print(f"{pastry_count} Pastries at $3 each: ${pastry_count * 3:.2f}")
    print(f"6% tax: ${tax:.2f}")
    print("---------")
    print(f"Total: ${total:.2f}")
    print("***************************************")
    print("Thank you for choosing Chris' Famous Coffee! We hope to see you again soon.")

def main():
    print("***************************************")
    print("Welcome to Chris Famous Coffee!")
    
    # Input number of items
    coffee_count = int(input("Number of coffees bought?\n"))
    muffin_count = int(input("Number of muffins bought?\n"))
    croissant_count = int(input("Number of croissants bought?\n"))
    pastry_count = int(input("Number of pastries bought?\n"))
    
    # Calculate total, subtotal, and tax
    total, subtotal, tax = calculate_total(coffee_count, muffin_count, croissant_count, pastry_count)
    
    # Display receipt
    display_receipt(coffee_count, muffin_count, croissant_count, pastry_count, total, subtotal, tax)

if __name__ == "__main__":
    main()

