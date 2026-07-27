food = input("What type of food do you want? ").lower()
budget = input("Do you want a cheap meal? (yes/no): ").lower()

if food == "pizza" and budget == "yes":
    print("You should try a budget-friendly pizza place.")
elif food == "pizza":
    print("You should try a nicer pizza restaurant.")
elif food == "burger":
    print("You should try a burger restaurant.")
else:
    print("You should try a local restaurant.")