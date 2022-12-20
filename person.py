#!/usr/bin/env python3

#Methods, Class

class Person():

    Gender = 'Male'

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_name(self):
        return self.name

    def change_name(self, name):
        self.name = name

    def get_age(self):
        return self.__age

    def change_age(self, age):
        self.__age = age

    def __str__(self):
        return self.name

# p1 = Person('Tom', 20)
# print(p1)
# print(type(p1))
# print(p1.get_name())
# print(p1.name)

# Class variable vs Instance variable
# p2 = Person('Jessi', 18)
# print(p1, p2)
# print(p1.Gender, p2.Gender)
# p2.Gender = 'Female'
# print(p1.Gender, p2.Gender)


#inheritance
class Student(Person):
    def __init__(self, name, age, score):
        super().__init__(name, age)
        self.score = score

    #Override
    # def get_name(self):
    #      return 'Name is ' + self.name

    def __get_score(self):
        return self.score

    def helper_score(self):
        return self.__get_score()
#
# stu = Student('john', 18, 100)
# print(stu.get_name())


#encapsulation

# # private variable
# p1 = Person('Tom', 20)
# print(p1.name)
# print(p1.age)
#  print(p1.get_age())

# private method
# print(stu.__get_score())
# print(stu.helper_score())


#Polymorphism
#
# different parameters
#
# range(1,10)
# range(1,10,2)
#
# def func(para1, para2, para3=3):
#     return para1*para2*para3
#
# print(func(1,2))
# print(func(1,2,4))


#Different Types
# len([1,2,3])
# len('123')
# 1 + 5
# [1,2] + [3,4]

#Polymorphism overriding
class shape():
    def get_size(self, length):
        pass

class rectangle(shape):
    def get_size(self, length):

        return length ** 2

class circle(shape):

    def get_size(self, radius):
        return 3.14 * radius ** 2 * 1 / 2
#
# rec = rectangle()
# print(rec.get_size(1))
#
# cir = circle()
# print(cir.get_size(1))






