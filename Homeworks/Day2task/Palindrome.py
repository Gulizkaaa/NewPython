# num = input("Please provide your number?: ")
# if num == '11' or num == '22' or num == '111' or num == '121' or num == '151' or num == '141':
#     print("True")
# else:
#     print("False")


num = input("Please provide your number?: ")

if num == num[::-1]: #it takes the number and checks whether number will be equal if we reverse it or not
    print("True")
else:
    print("False")