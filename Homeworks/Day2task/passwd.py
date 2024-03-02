import re
while True:
    password = input("Please enter the password?: ")
    if len(password) < 8: 
        print("Password should be more than 8 characters! Please provide valid password.")
    elif not re.search('[a-z]', password):
        print("Password should have at least one lowercase letter! Please provide valid password.")
    elif not re.search('[A-Z]', password):
        print("Password should have at least one uppercase letter! Please provide valid password.")
    elif not re.search('[0-9]', password):
        print("Password should have at least one digit! Please provide valid password.")
    elif not re.search('[!@#$%^&*()]', password):
        print("Password should have at least one special character! Please provide valid password.")
    else:
        print("Password accepted!")
    break
