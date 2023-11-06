# Get user input for 'small' and 'green'
small_input = input("Is it small? (True/False): ").lower()
green_input = input("Is it green? (True/False): ").lower()

# Convert user input to boolean values
small = small_input == 'true'
green = green_input == 'true'

# Check which items match the choices
if small and green:
    print("This matches: pea")
elif small and not green:
    print("This matches: cherry")
elif not small and green:
    print("This matches: watermelon")
elif not small and not green:
    print("This matches: pumpkin")
else:
    print("No match found")
