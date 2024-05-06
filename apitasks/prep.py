
# z = y = x = 1
# print(x, y, z, sep='*')

# x = input()
# y = input()
# print(x + y)

# x = 4
# y = 6
# z = x
# x = y
# y = z

# print (x, y)

# print("Hello, World!")

# print(7//9**0)

# var = 10.4
# var = int(var)
# print(var)

# word = 'Hello, World.'
# print(word[7:])

# hash = 1

# while hash <= 6:
# 	hash += hash
# 	print('#', end='')
# else:
# 	print('#')

# num = 3

# while num < 6:
#   print('Hello')
#   num = num + (num - 2)

# pet="dog"
# for i in range(0,len(pet)):
#     print(pet[i])

# num1 = 10
# num2 = 8
# num3 = 12
# if num1 < num2:
#    if num1 < num3:
#        print('smallest is:', num1)
# elif num2 < num1:
#    if num2 < num3:
#        print('smallest is:', num2)
# elif num3 < num1:
#    if num3 < num2:
#        print('smallest is:', num3)
# else:
#    print('else')


# def swap(num1, num2):
#     temp = num1;
#     num1 = num2;
#     num2 = temp;

# num1 = (2)
# num2 = (5)
# swap(num1, num2)
# print(num1 , num2)


# def f(i):
#     if i > 2:
#         return i
#     else:
#         return f(0) * f(3)

# print(f(2))

# nums = [1, 2, 3]

# vals = nums

# del vals[1:2]
# print(vals)

# lst1 = [1, 2, 4, 8]
# list2 = [2, 8, 4, 1]
 
# print(lst1 == list2)

# list = [3, 5, 7]
# list.insert(0, 4)
# list.append(6)
# print(list)

# def f1():
#    c = 30,
#    d = 20,

#    return c, d

# a, b = f1()
# print(a,b)


# p = '*'
# def multiply():
#   global p
#   p *= 3
#   print(3 * p)
# multiply()
# print(p)

# def outer():
#    lst = [1,2,3,4,5,6]
#    def inner():
#        lst[-1] = 0
#        print(lst)
#    inner()
#    print(lst)
# outer()


# x = [
#     'a',
#     'b',
#     {
#         'one': 1,
#         'two':
#         {
#             'x' : 10,
#             'y' : 20,
#             'z' : 30
#         },
#         'three': 3
#     },
#     'c',
#     'd'
# ]

# print(30 in x[2])


# x=0
# y=2
# z = len("Python") 
# x=y>z
# print(x)

# lst = ["A", "B", "C", 2, 4]
# del lst[0:-2]
# print(lst)

# x=0
# try:
#     print(x)
#     print(1 / x)
# except ZeroDivisionError:
#     print("ERROR MESSAGE")
# finally:
#     print(x + 1)
# print(x + 2)


# for i in range(1, 3):
# 	print("*", end="")
# else:
# 	print("*")


# def fun(x, y, z):
#     return x + 2 * y + 3 * z

# print(fun(0, z=1, y=3))


# others = 0
# for i in range(2):
#     for j in range(2):
#         if i != j:
#             others += 1
# else:
#     others += 1
# print(others)

# power = 1
# while power < 5:
#     power += 1
#     print("@")
#     if power == 3:
#         break
# else:
#     print("@")


# angle = 0
# for i in range(5):
#     if i % 2 == 1:
#         angle += 1
# else:
#     angle -= 1
# print(angle)

# others = -1
# for i in range(1,2):
#     for j in range(1,2):
#         if i == j:
#             others += 1
#     else:
#         others += 1
# print(others)


# for i in range(4):
#     if i % 2 == 1:
#         continue
#     print(i, end=' ')
# else:
#     print('FINISHED')

# 


# the_list = ['a', 'b', 'c']
# counter = 0
# for ix in range(len(the_list)):
#     print(the_list[ix], end=' ')
#     the_list[ix] = counter
#     counter += 1
# for ix in range(len(the_list)):
#     print(the_list[ix], end=' ') chatGPT

# list_one = [1,2]
# list_two = list_one[:]
# list_two.append(3)
# print(list_one[-1])

# user_data = ('John', 'American', 1964, [77.0, 78.2, 77.5])
# #user_data[3].append(79.3)
# user_data[3].insert(0,79.3)
# print(user_data)

# def process(data):
#     # data = [1,2,3]
#     data[1] = 2
#     return data[-2]

# measurements = [0 for i in range(3)]
# process(measurements)
# print(measurements[-2])

# def combine(width, height=2, depth=0, is_3D=False):
#     return (is_3D, width,height, depth)

# print(combine(1)[2])

# def walk(stop, start=1):
#     print(start, end='')
#     if start + 1 < stop:
#         walk(stop, start + 1)

# walk(3)

i = 1 ** 2 - 4 // 3
print(i)