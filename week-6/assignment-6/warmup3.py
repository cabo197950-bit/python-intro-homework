def create_message():
    message = "Hello from inside the function"
    print(message)


create_message()

# This would cause a NameError because message only exists inside create_message():
# print(message)
# NameError: name 'message' is not defined


def get_message():
    message = "Hello from inside the function"
    return message


result = get_message()
print(result)