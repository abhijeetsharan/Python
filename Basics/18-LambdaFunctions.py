# Lambda functions are small, one-line functions without a name.

add = lambda x, y: x + y
print(add(5, 3))

# Lambda wit map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)

#Lambda with filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)