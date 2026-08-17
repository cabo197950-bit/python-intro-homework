while True:
    try:
        number = int(input("Enter a positive integer: "))

        if number > 0:
            print(f"Got it: {number}")
            break
        else:
            print("That's not a positive integer. Try again.")

    except ValueError:
        print("That's not a positive integer. Try again.")