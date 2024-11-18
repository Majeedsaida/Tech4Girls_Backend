items = ["apple", "banana", "cherry"]
try:
    index = int(input("Enter the index of the item you want to access: "))
    print("You selected:", items[index])
except ValueError:
    print("Invalid input! Please enter a valid integer.")
except IndexError:
    print("Index out of range! Please enter an index between 0 and", len(items) - 1)