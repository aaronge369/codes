#!/usr/bin/env python3

#Day 3

#Pass by object reference

# num1 = 5
# num2 = num1
# print(id(num1), id(num2))
# #
# num2 = num2 + 1
# print(num1, num2)
# print(id(num1), id(num2))

#shared reference

# list1 = [1,2,3,4]
# list2 = list1
# list2.append(5)
# print(list1, list2)
# print(id(list1), id(list2))
#
# list2 = [2,3,4,5]
# print(list1, list2)
# print(id(list1), id(list2))

#
# a = (1,2,3)
# b = (1,2,3)
# print(id(a), id(b))




#Modules

# import Module as mo
# mo.func()

# from Module import func
# func()
#
# print(Module.var)







# # Lambda

# list1 = [1, 2, 3]
#
# mapping = map(lambda x: x*2 , list1)
# print(list(mapping))
#
# a = [10, -20, 30, 40, 50]
# a.sort()
# print(a)
#
# a.sort(key = lambda x : x**2)
# print(a)

#
# def power(x):
#     return x ** 2
#
# a = [1,2,-3]
# print(max(a, key = lambda x:x**2))
# print(max(a, key = power))





# # recursion

# def sum(s):
#
#     if s == 1:
#         return 1
#
#     return s + sum(s - 1)
#
# print(sum(3))


# 1 1 2 3 5 8 13 21 ..

# def fib(x):
#     if x == 1 or x == 2:
#         return 1
#
#     return fib(x-1) + fib(x-2)
#
# print(fib(7))
#
# def fib2(x):
#     temp = 0
#     num1 = 1
#     num2 = 1
#     i = 3
#
#     while i <= x:
#         temp = num1
#         num1 = num2 + num1
#         num2 = temp
#         i+=1
#
#     return num1
#
# print(fib2(7))