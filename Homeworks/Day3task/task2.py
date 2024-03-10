# sum = 0.0
# for num in range(51):
#     if num % 2 == 1:
#         sum = sum + num
# print(sum)


sumeven = 0.0
sumodd = 0.0
lst = [] # this list is empty 
for num in range(51):
    lst.append(num) # with this function we are adding the content of num to the list
    if num % 2 == 0:
        sumeven = sumeven + num
    elif num % 2 == 1:
       sumodd = sumodd + num

print("The sum of even numbers is:", sumeven)        
print("The production of odd numbers is:", sumodd)
print("The largest number is:", max(lst))

# lst = [num for num in range(1, 11)]  -----> the value you want to append should come first 

# sumeven = 0.0
# sumodd = 0.0

# lst = [num if num % 2 == 0 elif num % 2 == 1 for num in range(1,51)]
#     sumeven = sumeven + num
#     sumodd = sumodd + num

# print("The sum of even numbers is:", sumeven)        
# print("The production of odd numbers is:", sumodd)
# print("The largest number is:", max(lst))



