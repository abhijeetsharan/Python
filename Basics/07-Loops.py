# For loop
for i in range(1, 6):
    print("Number:", i)

# While loop
count = 1
while count <= 5:
    print("Count:", count)
    count += 1


# Break and continue
for i in range(1, 6):
    if i == 3:
        break
    print(i)

for i in range(1, 6):
    if i == 3:
        continue
    print(i)