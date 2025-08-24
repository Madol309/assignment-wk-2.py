# empty list 
my_list = []

# append values to list (use extend for multiple values)
my_list.extend([10, 20, 30, 40])
print(my_list)

# insert value 15 at the second position in the list (index 1)
my_list.insert(1, 15)
print(my_list)

# extend my_list by adding 50, 60, 70
my_list.extend([50, 60, 70])
print(my_list)

# remove the last number from the list
my_list.pop()
print(my_list)

# sort my_list in ascending order
my_list.sort()
print(my_list)

# find and print the index of 30 in my_list
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)


