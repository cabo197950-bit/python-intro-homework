first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

try:
    result = first_number / second_number
    print(f"The result is: {result}")
except ZeroDivisionError:
    print("You cannot divide by zero.")