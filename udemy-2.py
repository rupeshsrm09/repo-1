import random

health = 50
difficulty = 1
potion_health = int(random.randint(25,50) / difficulty)
health = health + potion_health
print(health)

# Creating a list
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "apple", True, 3.14]

print(fruits)       # Output: ['apple', 'banana', 'orange']
print(numbers)      # Output: [1, 2, 3, 4, 5]
print(mixed_list)   # Output: [1, 'apple', True, 3.14]

# indexing
fruits = ["apple", "banana", "orange"]
print(fruits[0])     # Output: apple
print(fruits[1])     # Output: banana
print(fruits[2])     # Output: orange

# Slicing
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])

# list are mutable

fruits = ["apple", "banana", "orange"]
fruits[1] = "grape"
print(fruits)

# operations on list . - append, add, insert, remove , find, sort
# Append

fruits = ["apple", "banana", "orange"]
fruits.append("grape")
print(fruits)

# slicing
# test
