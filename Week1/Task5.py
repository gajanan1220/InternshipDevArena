# 1. Creating a List
fruits = ["apple", "banana", "mango", "orange"]

# 2. Accessing Items (using index)
print("First item:", fruits[0])      # apple
print("Third item:", fruits[2])      # mango

# 3. Changing an Item
fruits[1] = "grapes"
print("Updated list:", fruits)

# 4. Adding Items
fruits.append("pineapple")
print("After append:", fruits)

# 5. Removing Items
fruits.remove("mango")
print("After remove:", fruits)

# 6. Length of List
print("Total items:", len(fruits))

# 7. Slicing a List
print("First two fruits:", fruits[0:2])

# 8. Checking if an item exists
print("Is apple in list?", "apple" in fruits)
