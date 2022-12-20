#!/usr/bin/env python3

#Day 1

# String

#''
#str()

# str1 = 'string'
# str2 = "string"
# str3 ="""str
# ing"""
# print(str1)
# print(str2)
# print(str3)


# Indexing

# str1 = '123'
# print(str1[0])
# print(str1[2])
# print(str1[-3])
# print(str1[3]) #Index out of bound error

# Slicing

# str1 = [1,2,3,4,5]
# print(str1[1:]) #take all elements except first
# print(str1[:-1]) #take all elements except last
# print(str1[0::2]) #take elements starting from 0 and skip every 2 elements till the end
# print(str1[-1::-2]) #take elements starting from last element and skip every 2 elements till the beginning
# print(str1[:1:-2])

# + and * operator

# str1 = 'string'
# str2 = ' extension'
# print(str1 + str2)
# print(str1 * 3)


#Format

# str1 = 'string'
# str2 = '7'
# str3 = 'this is a {} with {} words'.format(str1, str2)
# print(str3)
# str4 = 'this is a {1} with {0} words'.format(str1, str2)
# print(str4)
# str5 = 'this is a {first} with {second} words'.format(first = str1, second = str2)
# print(str5)
# str6 = f'this is a {str1} with {str2} words'
# print(str6)


#Variables

# some_integer = 5
# some_string = 'string'
# some_float = 1.1111

# #can assign multiple values

# int1 = int2 = int3 = 3
# str1, str2, str3 = 'str1', 'str2', 'str3'
# print(int1,int2,int3)
# print(str1,str2,str3)

#
# print("Integer -> {} \n String -> {}\n Float -> {}\n".format(some_integer, some_string, some_float))

# Booleans

# num1 = 5
# print(bool(0.00))
# str1 = ''
# print(bool(str1))
# str2 = 'abd'
# print(bool(str2))
# print(bool(None))
# print(1>2, 1==2, 1<2, 1>=2, 1<=2, 1!=2)

# if else
#
# list1 = '12345'
# if len(list1) < 4 or len(list1) > 6:
#     print('length is not 5')
# elif len(list1) == 5:
#     print('length is 5')
# else:
#     print('don\'t know the length')


# For loop

# print(range(1,10))
# for i in range(1,10):
#     print(i)
#
# summ = 0
# for i in range(10):
#     summ += i
# print(summ)

# # enumerate

# str1 = 'abcde'
# for item in enumerate(str1):
#     print(item)
#     print(item[0], item[1])

# for (index, item) in enumerate(str1):
#     print(index, item)

# Nested For loop

# for i in range(3):
#     for j in range(3):
#         print(i,j)


#Continue vs Break
#
# cont = []
# for i in range(10):
#     if i == 5:
#         continue
#     cont.append(i)
#
# bre = []
# for i in range(10):
#     if i == 5:
#         break
#
#     bre.append(i)
#
# print(cont, bre)


# While Loop

# i = 0
# while i < 10:
#     print(i)
#     i += 1


#Sign
# print(-5//2)
# print(-5//-2)

# print('\n')
# print(-5%2)
# print(-5%-2)
# print(5%2)
# print(5%-2)

# Function
# def sample_function(inp1):
#     return inp1
#
# print(sample_function(3))

#Parameters
# def sample_func(inp1, inp2, inp3 = 4):
#     return inp1*inp2*inp3
#
# result = sample_func(1,2)
# print(result)


# def sample_func(*input1):
#     output = 1
#     for i in input1:
#         output *= i
#     return output
#
# result = sample_func(1,2,3)
# print(result)

# def some_func():
#     pass

#local vs global

# def global_local():
#     global loc
#     loc = 5
#     loc *= 5
#     return loc
#
# global_local()
# print(loc)

# def user_inp(user_input):
#     print(f'User entered {user_input}')

#Input

# user_input = input('Please enter a number:')
# print(f'User entered {user_input}')

# user_inp(user_input)

# user_input = input('Please enter a number:')
# user_input + 10



# List

# # Create empty list
# sample_list = []
# sample_list2 = list()
# print(sample_list,sample_list2)

# # Create non-empty list
# sample_list3 = [1, 2.5,'list', [1,2,3]]
# sample_list4 = list([1, 2.5, 'list', [1,2,3]]) #nested list
# print(sample_list3, sample_list4)

# Change element in list
# list1 = [1,2,3,4,5]
# list1[2:4] = [-3,-4]
# print(list1)

# Append an element in list
# list1 = [1,2,3,4,5]
# list1.append(6)
# print(list1)

# Insert an element into list
# list1 = [1,2,3,4,5]
# list1.insert(1,'first')
# list1.insert(1,'second')
# print(list1)
# list1 = [1,2,3,4,5]
# list1.count(1)         # How many times is 1 in list1
# list1.index(1)          # Find index of first 1 in list1
# list1.reverse()         #reverse the list1
# list1.sort()            #sort the list1
# list1.remove(1)        # Remove the first 1 in the list

# list1 = [1,2,3,4,'a']
# list1 = list1 + [6,7,8]
# print(list1)

# l1 = [1,2,3]
# print(l1 * 3)
# print(l1 + l1)

# List Comprehension

# get all even numbers
# list1 = [1,2,3,4,5]
#
# list2 = [i for i in list1 if i % 2 == 0]
#
# print(list2)
# # # equavelent to
#
# list3 = []
# for i in list1:
#     if i%2 == 0:
#         list3.append(i)
# print(list3)

#get all even numbers and raise to power of 2, otherwise turn the number to 0
# list4 = [i if i % 2 == 0 else 0 for i in range(1,10)]
# print(list4)


# Split
# print('This is a string.'.split(' '))

# Dynamic Typing

#This is a comment


'''
this
is a multipleline
comment
'''



