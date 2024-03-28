# Bottle Return Program
# Author: Chris Lopez
# Date: March 27th, 2024
# Description: This program allows a grocery store to keep track of the total number of bottles collected for seven days. 

# Step 1: Declare variables below 
total_bottles = 0
counter = 1
today_bottles = 0
total_payout = 0.0
keep_going = "y"

# Step 2: Loop to run program again
while keep_going == "y":
    # Step 3: Code to set value of variables
    total_bottles = 0
    total_payout = 0.0
    
    # Code to get bottles returned for each day
    NBR_OF_DAYS = 7
    while counter <= NBR_OF_DAYS:
        today_bottles = int(input(f"Enter number of bottles returned for day #{counter}: "))
        total_bottles += today_bottles
        counter += 1

    # Calculate total payout
    PAYOUT_PER_BOTTLE = 0.10
    total_payout = total_bottles * PAYOUT_PER_BOTTLE

    # Display total number of bottles collected and total payout
    print("\nThe total number of bottles collected is:", total_bottles)
    print("The total paid out is $", total_payout)

    # Ask if the user wants to enter another week's worth of data
    keep_going = input("\nDo you want to enter another week’s worth of data?\n(Enter y or n): ")

