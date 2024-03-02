
password = input("Please enter the password?: ")

for letters in password:
    if len(password) < 8: 
        print("Password should be more than 8 characters! Please provide valid password.")
    else:
        print("Invalid password! Please try one more time")

