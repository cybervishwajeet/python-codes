class IncorrectPasswordError(Exception):
    pass

def check_password(password):
    correct_password = "theoislegitvedant"  # Replace with the correct password

    if password != correct_password:
        raise IncorrectPasswordError("Incorrect password!")

    print("Password is correct!")

try:
    user_password = input("Enter the password: ")
    check_password(user_password)
except IncorrectPasswordError as e:
    print(e)
else:
    print("Password is correct!")
