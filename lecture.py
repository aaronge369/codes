#!/usr/bin/env python3

#Day 1

#List

# # Create empty list
# sample_list = []
# sample_list2 = list()
# print(sample_list,sample_list2)

# # Create non-empty list
# sample_list3 = [1, 2.5,'list', [1,2,3]]
# sample_list4 = list([1,2.5,'list', [1,2,3]]) #nested list
# print(sample_list3, sample_list4)

# # Indexing
# str1 = '123'
# print(str1[0])
# print(str1[2])
# print(str1[-1])
# print(str1[3]) #Index out of bound error

# Slicing
# str1 = [1,2,3,4,5]
# print(str1[1:]) #take all elements except first
# print(str1[:-1]) #take all elements except last
# print(str1[0::2]) #take elements starting from 0 and skip every 2 elements till the end
# print(str1[-1::-2]) #take elements starting from last element and skip every 2 elements till the beginning
# print(str1[:1:-2])


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

# list1 = [1,2,3,4,5]
# list1 = list1 + [6,7,8]
# print(list1)

#String

# s1 = 'string'
# s2 = "string"
# s3 ="""str
# ing"""
# print(s1)
# print(s2)
# print(s3)

# + and * operator
# s1 = 'string'
# s2 = ' extension'
# print(s1 + s2)
# print(s1 * 3)

#also works on list
# l1 = [1,2,3]
# print(l1 * 3)
# print(l1 + l1)


#Format

# str1 = 'string'
# str2 = 7
# str3 = 'this is a {} with {} words'.format(str1, str2)
# print(str3)
# str4 = 'this is a {1} with {0} words'.format(str1, str2)
# print(str4)
# str5 = f'this is a {str1} with {str2} words'
# print(str5)


#Variables

# some_integer = 5
# some_string = 'Beacon Fire'
# some_float = 1.1111

# #can assign multiple values

# int1 = int2 = int3 = 3
# str1, str2, str3 = 'str1', 'str2', 'str3'
# print(int1,int2,int3)
# print(str1,str2,str3)

#
# print("Integer -> {} \n String -> {}\n Float -> {}\n".format(some_integer, some_string, some_float))

#Dynamic Typing

#Booleans

# num1 = 5
# print(bool(5))
# str1 = ''
# print(bool(str1))
# print(bool(None))
# print(1>2, 1==2, 1<2, 1>=2, 1<=2, 1!=2)


#if else

# list1 = [1,2,3,4,5]
# if len(list1) < 4 or len(list1) > 6:
#     print('length is not 5')
# elif len(list1) == 5:
#     print('length is 5')
# else:
#     print('don\'t know the length')



#For loop

# print(range(1,10))
# for i in range(1,10):
#     print(i)

#enumerate

# list1 = ['a','b','c','d','e']
# for item in enumerate(list1):
#     print(item)
#     print(item[0], item[1])
#
# for (index, item) in enumerate(list1):
#     print(index, item)

# Nested For loop

# for i in range(3):
#     for j in range(3):
#         print(i,j)


#Continue vs Break

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
#     bre.append(i)
#
# print(cont, bre)

#While Loop

# i = 0
# while i < 10:
#     print(i)
#     i += 1

#This is a comment
'''
this
is a multipleline
comment
'''

#Day 2


#Dictionary

# dic1 = {1 : 'a', 2: 'b', 'abc': 'c' }
# print(dic1)
# print(dic1.items())
# print(dic1.keys())
# print(dic1.values())
# print(1 in dic1)
# print(1 in dic1.keys())

#unique key values
# dic1[1] = 'd'
# print(dic1)

#immutable key value
# dic1[[1,2,3]] = 'e'

#Loop through dictionary
# dic1 = {1 : 'a', 2: 'b', 'abc': 'c' }
# for key in dic1:
#     print(key, dic1[key])

#Tuple

#create a tuple
# tup1 = (1,2,3)
# tup2 = tuple((1,2,3))
# tup3 = 1,
# print(tup1)
# print(tup2)
# print(tup3)

#unpack a tuple
# tup1 = (1,2,'3')
# num1, num2, str1 = tup1
# print(num1 + num2, str1 + '4')


#Set

# set1 = {1,1,2,3}
# set2 = set((1,2,3))
# print(set1)
# print(set2)

# # unordered

# set1.add('123')
# set1.add(1.5)
# for i in set1:
#     print(i)

#set operations

# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7,8}
# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.difference(set2))
# print(set1.symmetric_difference(set2))

#casting

#int to float
# int1 = 1
# float1 = float(int1)
# print(float1)

#float to int
# float2 = 1.5
# int2 = int(float2)
# print(int2)

#int to string
# int3 = 123
# string1 = str(int1)
# print(string1)

#string to int
# string2 = '123'
# int4 = int(string2)
# print(int4)

#What happened in this situation?
# string3 = '123a'
# int5 = int(string3)


# list to set
# list1 = [1,2,2,3,4,5,6,6]
# set1 = set(list1)
# print(set1)

# binery to int
# binery1 = '0101'
# int5 = int(binery1, 2)
# print(int5)

# Stack vs Queue
#
#
#
#
#

# List Comprehension

# get all even numbers
# list1 = [1,2,3,4,5]
# list2 = [i for i in list1 if i %2 == 0]
# print(list2)
# #equavelent to
# list3 = []
# for i in list1:
#     if i%2 == 0:
#         list3.append(i)
#
# #get all even numbers and raise to power of 2, otherwise turn the number to 0
# list4 = [i ** 2 if i % 2 == 0 else 0 for i in range(1,10)]
# print(list4)

# #dictionary comprehension
# dic1 = {1:'a',2:'b',3:'c'}
# dic2 = {item[0]+10 : 'new_' + item[1] for item in dic1.items()}
# print(dic1)
# print(dic2)


#Day 3

#Pass by object reference

#shared reference
# list1 = [1,2,3,4]
# list2 = list1
# list2 = [1,2,3,4]
# print(list2)
# print(list1)


#Functions



# Lambda
# a = [1, 2, 3]
#
# gg = map(lambda x: x*2 , a)
# print(list(gg))
#
# a = [10, -20, 30, 40, 50]
# a.sort()
# print(a)
#
# a.sort(key = lambda x : x**2)
# print(a)
#
# a = [1,2,-3]
# print(max(a, key = lambda x:x**2))
#


# Day 4

#Escape characters
# print('\\')
# print('abc\ndef')
# print('abc\'string\'def')


# File handling
#
# file1 = open('./demo.txt')
# print(file1.readlines())
# print(file1.readlines())
# for line in file1.readlines():
#    print(line)

# file2 = open('./demo.txt', 'a')
# file2.write('add a new line\n')
# file2.close()
#
# file3 = open('./demo.txt', 'r')
# print(file3.readlines())














