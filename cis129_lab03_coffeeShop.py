# Author : Chris Lopez
# Coffee Shop Simulator

# Function to calculate total cost with tax
def calculate_total(coffee_count, muffin_count):
    coffee_price = 5
    muffin_price = 4
    tax_rate = 0.06
    
    coffee_cost = coffee_count * coffee_price
    muffin_cost = muffin_count * muffin_price
    
    subtotal = coffee_cost + muffin_cost
    tax = subtotal * tax_rate
    total = subtotal + tax
    
    return total, subtotal, tax

# Function to display the receipt
def display_receipt(coffee_count, muffin_count, total, subtotal, tax):
    print("***************************************")
    print("My Coffee and Muffin Shop Receipt")
    print(f"{coffee_count} Coffee at $5 each: ${coffee_count * 5:.2f}")
    print(f"{muffin_count} Muffins at $4 each: ${muffin_count * 4:.2f}")
    print(f"6% tax: ${tax:.2f}")
    print("---------")
    print(f"Total: ${total:.2f}")
    print("***************************************")

def main():
    print("***************************************")
    print("My Coffee and Muffin Shop")
    
    # Input number of coffees and muffins
    coffee_count = int(input("Number of coffees bought?\n"))
    muffin_count = int(input("Number of muffins bought?\n"))
    
    # Calculate total, subtotal, and tax
    total, subtotal, tax = calculate_total(coffee_count, muffin_count)
    
    # Display receipt
    display_receipt(coffee_count, muffin_count, total, subtotal, tax)

if __name__ == "__main__":
    main()
