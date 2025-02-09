names = ["Abhijeet", "Shivam", "Rishabh", "Rishi"]
print(names)
print("Length of the list is: ", len(names))
print(names[-1]) 
print(names[::-1]) #Reverse

names.append("Vinayak")
print(names)

for name in names:
    print(name)