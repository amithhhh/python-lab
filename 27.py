import re

# User ID pattern:
user_pattern = r'^[A-Z][A-Za-z0-9\-_@]{0,7}$'

# Password pattern (exactly one digit):
password_pattern = r'^(?=[^0-9]*[0-9][^0-9]*$).+$'

userid = input("Enter User ID: ")
password = input("Enter Password: ")

# Validate User ID
if re.match(user_pattern, userid):
    print("Valid User ID")
else:
    print("Invalid User ID")

# Validate Password
if re.match(password_pattern, password):
    print("Valid Password")
else:
    print("Invalid Password")
