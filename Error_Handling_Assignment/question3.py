try:
    user_input = input("Enter a number: ")
    converted_number = int(user_input)
    print("The number you entered is:", converted_number)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
