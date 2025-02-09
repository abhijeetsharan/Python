try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result: ", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
except ValueError:
    print("Error: Please enter a valid number!")
finally:
    print("Execution Completed")