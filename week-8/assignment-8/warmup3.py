try:
    file = open("missing_file.txt", "r")
    contents = file.read()
    print(contents)
    file.close()

except FileNotFoundError:
    print("The file was not found.") 