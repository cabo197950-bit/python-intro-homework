try:
    with open("../data/missing.txt", "r") as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print("The file could not be found. Please check the file path.")