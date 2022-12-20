#!/usr/bin/env python3

#Day 2

# Tuple

# # create a tuple
# tup1 = (1,2,3)
# tup2 = tuple((1,2,3))
# tup3 = (1)
# tup4 = 1,
# print(tup1)
# print(tup2)
# print(tup3)
# print(tup4)

# # Unpack a tuple

# tup1 = (1,2,'3')
# num1, num2, str1 = tup1
# print(num1 + num2, str1 + '4')
#
#
# num1, *list1 = tup1
# print(num1, list1)

# Can also use + and * same as list



#Dictionary

# dic1 = {1 : 'a', 2: 'b', 'abc': 'c' }
# print(dic1)
# print(dic1.items())
# print(dic1.keys())
# print(dic1.values())
#
# print(1 in dic1)
# print(1 in dic1.keys())


#unique key values

# dic1 = {2:'b'}
# dic1[1] = 'e'
# dic1[1] = 'f'
#
# print(dic1)

#immutable key value
# dic1 = {}
# # dic1[[1,2,3]] = 'e'
#
# dic1[(1,2,3)] = 'e'

# #Loop through dictionary
# dic1 = {1 : 'a', 2: 'b', 'abc': 'c' }
#
# for key in dic1.keys():
#     print(key, dic1[key])
#
# for key in dic1:
#     print(key, dic1[key])
#
# for value in dic1.values():
#     print(value)
#
# for item in dic1.items():
#     print(item[0], item[1])

# #dictionary comprehension

# dic1 = {1:'a',2:'b',3:'c'}
# dic2 = {item[0]+10 : 'new_' + item[1] for item in dic1.items()}
# print(dic1)
# print(dic2)


#Set


# dict1 = {}
# dict1[1] = 'a'
# dict1[2] = 'b'
# dict1[3] = 'c'
# for i in dict1:
#     print(i, dict1[i])


# set1 = {1,1,2,3}
# set2 = set((1,2,3))
# print(set1)
# print(set2)

# set1 = set()
# print(type(set1))

#
# # unordered
#
# set1.add('123')
# set1.add(1.5)
# set1.add((1,2,3))
#
# for i in set1:
#     print(i)

# Set operations

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
# str1 = str(int3)
# print(str1)

#string to int
# str2 = '123'
# int4 = int(str2)
# print(int4)

#What happened in this situation?
# string3 = '123a'
# int5 = int(string3)
# print(int5)

# list to set
# list1 = [1,2,2,3,4,5,6,6]
# set1 = set(list1)
# list1 = list(set1)
# print(list1)

# binery to int
# binery1 = '0101'
# int5 = int(binery1, 2)
# print(int5)




# Stack vs Queue
#


