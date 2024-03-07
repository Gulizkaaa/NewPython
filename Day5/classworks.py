
# def checkEven(num):  # here we are defining the function and when we are defininf the value we call it parameter
#     if num % 2 == 0:
#         return "This is even" #------> return always returns the data type 
#     else:
#         return "This is odd"

# even = 2
# print(checkEven(even))
# print(checkEven(89))

# def converter(celsius):
#     f = (celsius * 1.8) + 32
#     return f

# inp = float(input("Please provide the degree in celsius: "))
# print(converter(inp))

# def Oddfunction(num):
#     odd_lst = []
#     for i in num:
#         if i % 2 == 1:
#             odd_lst.append(i)
#     return odd_lst

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]     
# print(Oddfunction(lst))

# def wordchecker(lst, char):
#     word_lst = []
#     for word in lst:
#         if char in word:
#             word_lst.append(word)

#     return word_lst # however here we cannot return lst?

# fruits = ["mango", "apple", "banana"]
# print(wordchecker(fruits, "a"))

### function for addition #####
# def addition(num1, num2):
#     return num1 + num2

# inp1 = int(input("Please provide your number1:"))
# inp2 = int(input("Please provide your number2:"))
# print(addition(inp1, inp2))


### function for addition #####
def substraction(num1, num2): #- inp1 and inp2 are the parameters, we give parameters to reuse the function
    return num1 - num2 #why here we can return using the parameters

inp1 = int(input("Please provide your number1:"))
inp2 = int(input("Please provide your number2:"))
print(substraction(inp1, inp2))