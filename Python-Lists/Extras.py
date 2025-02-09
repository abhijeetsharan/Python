# List Comprehension (Shorter Syntax)

numbers = [1, 2, 3, 4 ,5]
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)

# Checking if an Item Exists
fruits = ["apple", "banana", "cherry"]
if "apple" in fruits:
    print("Apple is in the list")

# Joining List
list1 = [1, 2, 3]
list2 = [4, 5, 6]

merged = list1 + list2
print(merged)


# Splitting a string into a list
sentence = "Hello world this is Python"
words = sentence.split()
print(words)
