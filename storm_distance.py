while True:
    try:
        # Prompt the user to enter the time delay between the lightning and the thunder in seconds
        seconds = float(input("Enter the time delay between the lightning and the thunder (in seconds)\n"))
        
        # If the user has entered either zero or a negative number, prompt them to enter a valid input
        if seconds <= 0:
            print("Invalid entry, please enter a number greater than zero.")
            continue
        break
    except ValueError:
        # If the user has entered a non-numerical input, prompt them to enter a valid input
        print("Invalid entry, please enter a number greater than zero.")

# Calculate and display the storm distance, rounded to 2 decimals
print("The storm is " + str(round(seconds / 5, 2)) + " miles away.")

# In the end, prompt the user to press Enter, in order to exit the program
input("Press Enter to exit the program")