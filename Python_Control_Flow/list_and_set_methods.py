# list_and_set_methods.py

# List methods
my_list = [10, 20, 35, 40, 50]
my_list.append(55)
my_list.remove(20)
my_list.pop()
my_list.sort()
my_list.reverse()
my_list.extend([70, 80])

print("List after operations:", my_list)

# Set methods
my_set = {1, 2, 3, 4, 5}
my_set.add(6)
my_set.remove(2)
print("Union:", my_set.union({3, 6}))
print("Intersection:", my_set.intersection({3, 6}))
print("Difference:", my_set.difference({3, 4}))
