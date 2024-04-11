# Author: Chris Lopez 
# Title Theater Sitting Lab
# Date: April 10th, 2024
#    This program represents a system set in place for a movie theater's sitting arrangements and capacity with relation to the purchased tickets.

# Constants for ticket prices
PRICE_SECTION_A = 20
PRICE_SECTION_B = 15
PRICE_SECTION_C = 10

# Constants for section capacities
CAPACITY_SECTION_A = 300
CAPACITY_SECTION_B = 500
CAPACITY_SECTION_C = 200

# Constants for section names
SECTION_A = 'A'
SECTION_B = 'B'
SECTION_C = 'C'

# Display welcome message
print("Welcome to the Theater Seating Program!")
print(f"Section {SECTION_A}: ${PRICE_SECTION_A} per seat, {CAPACITY_SECTION_A} seats available")
print(f"Section {SECTION_B}: ${PRICE_SECTION_B} per seat, {CAPACITY_SECTION_B} seats available")
print(f"Section {SECTION_C}: ${PRICE_SECTION_C} per seat, {CAPACITY_SECTION_C} seats available")

def get_ticket_sales(section_name, section_price, section_capacity):
    """Function to get and validate the number of tickets sold for a section."""
    while True:
        try:
            tickets_sold = int(input(f"Enter the number of tickets sold for section {section_name}: "))
            if 0 <= tickets_sold <= section_capacity:
                return tickets_sold
            else:
                print(f"Please enter a number between 0 and {section_capacity}.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def calculate_income(tickets_sold, ticket_price):
    """Function to calculate income for a section."""
    return tickets_sold * ticket_price

def main():
    # Dictionary to hold section details
    sections = {
        SECTION_A: {'price': PRICE_SECTION_A, 'capacity': CAPACITY_SECTION_A, 'tickets_sold': 0},
        SECTION_B: {'price': PRICE_SECTION_B, 'capacity': CAPACITY_SECTION_B, 'tickets_sold': 0},
        SECTION_C: {'price': PRICE_SECTION_C, 'capacity': CAPACITY_SECTION_C, 'tickets_sold': 0},
    }

    total_income = 0

    for section in sections:
        tickets_sold = get_ticket_sales(section, sections[section]['price'], sections[section]['capacity'])
        sections[section]['tickets_sold'] = tickets_sold
        section_income = calculate_income(tickets_sold, sections[section]['price'])
        total_income += section_income
        print(f"Subtotal for section {section}: ${section_income:.2f}")

    # Display final totals
    print("\nFinal Totals:")
    for section in sections:
        print(f"Section {section}: {sections[section]['tickets_sold']} tickets sold, Subtotal: ${sections[section]['tickets_sold'] * sections[section]['price']:.2f}")
    print(f"Overall total income: ${total_income:.2f}")

if __name__ == "__main__":
    main()
