
### function for addition ###
def addition(num1, num2):
    return num1 + num2

# inp1 = int(input("Please provide your number 1:"))
# inp2 = int(input("Please provide your number 2:"))
# print(addition(inp1, inp2))

### function for substruction ###
def substraction(num1, num2): 
    return num1 - num2 
# inp1 = int(input("Please provide your number 1:"))
# inp2 = int(input("Please provide your number 2:"))
# print(substraction(inp1, inp2))

### function for multuplication ###
def multiplication(num1, num2): 
    return num1 * num2 
# inp1 = int(input("Please provide your number 1:"))
# inp2 = int(input("Please provide your number 2:"))
# print(substraction(inp1, inp2))

### function for division ###
def division(num1, num2): 
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    return num1 / num2 
# inp1 = int(input("Please provide your number 1 :"))
# inp2 = int(input("Please provide your number 2 :"))
# print(division(inp1, inp2))

print()
print("Welcome to the calculator program!")
print()
print("Please choose the operation: +, -, *, /")
print()
print ("--------------------------------------")
print()


num1 = float(input("Please provide your number 1: "))
num2 = float(input("Please provide your number 2: "))

while True:
    prompt = input("Please choose the operation (+,-,*,/): ") # take input from the user   
    if prompt in ('+', '-', '*', '/'):  # check if choice is one of the four options    
        if prompt == '+':
            print("Result of addition: ", addition(num1, num2))
        elif prompt == '-':
            print("Result of substruction: ", substraction(num1, num2))
        elif prompt == '*':
            print("Result of multiplication: ", division(num1, num2))
        elif prompt == '/':
            print("Result of division: ", num1 // num2)
        break
    else:
        print("Invalid Input")


### I have done this homework with the help of google and web page,
### www.programiz.com/python 