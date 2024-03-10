
def average(*args): # 
    total = sum(args)
    return total // len(args) #to have integer 
# we can use / to get float

print(average(10, 23, 45, 3, 8, 12, 45))
