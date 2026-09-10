while True:
    user_input = input("Enter a number: ")

    try:
        number = float(user_input)
        print(f"You entered: {number}")
        break
    except ValueError:
        print("That is not a valid number. Please try again.")