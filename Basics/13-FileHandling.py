# wriing to the file
with open("test.txt", "w") as file:
    file.write("Hello, Abhijeet!\nWelcome to Python.")

# Reading from a file
with open("test.txt", "r") as file:
    content = file.read()
    print(content)