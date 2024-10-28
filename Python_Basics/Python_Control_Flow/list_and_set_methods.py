# list_and_set_methods.py

# List methods
my_list = [10, 18, 35, 40, 62]
my_list.append(60)
my_list.remove(35)
my_list.pop()
my_list.sort()
my_list.reverse()
my_list.extend([75, 80])

print("List after operations:", my_list)

# Set methods
my_set = {1, 2, 3, 4}
my_set.add(5)
my_set.remove(2)
print("Union:", my_set.union({3, 6}))
print("Intersection:", my_set.intersection({3, 6}))
print("Difference:", my_set.difference({3, 4}))
