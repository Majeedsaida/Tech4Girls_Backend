# tuple_and_type_conversion.py

#example of  Tuple
my_tuple = (10, 20, "Hello", 40, "python")
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])
print("Count of 'Hello':", my_tuple.count("Hello"))
print("Index of 'python':", my_tuple.index("python"))

# Type conversion
num = 10
print("Float:", float(num))

decimal = 3.14
print("Integer:", int(decimal))

num_str = "50"
print("String to integer:", int(num_str))

# Join example
words = ["Python", "is", "fun"]
print("Joined string:", " ".join(words))
