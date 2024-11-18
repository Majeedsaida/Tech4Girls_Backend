data = {"name": "saida", "age": 20, "country": "America"}
try:
    key = input("Enter the key you want to look up: ")
    print("Value:", data[key])
except KeyError:
    print(f"Key '{key}' does not exist in the dictionary.")
