# # Tuple

# to store multiple data
# can store duplicate items

# differences
# 1. List -> [] Tuple -> ()
# 2. List is Mutable while tuple is immutable

# eg_list=[34,35,36,37]
# print(eg_list)
# eg_list[2]=45
# print(eg_list)

# eg_tuple=(34,35,36,37)
# print(eg_tuple)
# # eg_tuple[2]=45
# eg_tuple = (34,35,45,37)

# empty_tuple = ()
# mixed_tuple = (1,'Hi',4.45)

# Attributes in list

# eg_list = [1,2,3,4,5]
# print(len(eg_list)) #to find the length of the list
#
# eg_list.append(6) #to add a new item to the list
# print(eg_list)
#
# eg_list.remove(5) #to remove a value from list
# print(eg_list)
#
# print(min(eg_list)) #to find the minimum value in a list
# print(max(eg_list)) #to find the maximum value in a list

# > greater than
# print('5 > 3 =',5>3)
# print('3 > 5 =',3>5)

# < less than
# print('3 < 5 =',3<5)
# print('5 < 3 =',5<3)

# == value equals
# print('3 == 3',3==3)
# print('3 == 5',3==5)

# != value not equals
# print('3 != 5',3!=5)
# print('3 != 3',3!=3)

# >= greater than or equals
# print('5 >= 3',5>=3)
# print('5 >= 5',5>=5)
# print('3 >= 5',3>=5)

# <= lesser than or equals
# print('3 <= 5',3<=5)
# print('5 <= 5',5<=5)
# print('5 <= 3',5<=3)

# take input from the user asking for his/her birth year
#     calculate the age using that and print a statement
# that says "As your were born in 1994 your age is 30"

# Assignment operators
a = 10
# +=
a += 10 # a = a+10
# print(a)

# Logical operators

# and (Multiplication)
# True 1
# False 0

# print(True and True) #(1*1) True
# print(True and False) #False
# print(False and True) #False
# print(False and False) #False

# print(5>3 and 5>4) use case of logical operator

# or (addition)
# print(True or True) #(1+1) True
# print(True or False) #True
# print(False or True) #True
# print(False or False) #False

# not
# print(not True) #False
# print(not False) #True

# 0101011
# 0010101
# print(5 & 3)

# a=input('a=')
# b=input('b=')
# if (a>b):
#     print('a is greater than b')
#     print('if statement')
# else:
#     print('a is not greater than b')
#     print('else statement')

# if condition:
#     statement 1
# elif condition:
#     statement 2
# elif condition:
#     statement 3
# else:
#     statement 4

# Python program to segragate students into section based on age

# age = int(input('Age: '))
# if (age < 5):
#     print('Kindergarten')
# elif (age < 10):
#     print('Primary')
# elif (age < 15):
#     print('High school')
# elif (age < 18):
#     print('Higher secondary')
# else:
#     print('Does not belong in school')

# Python program to play Rock Paper Scissors

# p1 = input('Enter Rock(r) or Paper(p) or Scissors(s)').lower()[0]
# p2 = input('Enter Rock(r) or Paper(p) or Scissors(s)').lower()[0]
#
# if (p1 == 'r' and p2=='p'):
#     print('player 2 wins')
# elif (p1 == 'p' and p2=='r'):
#     print('player 1 wins')
# elif (p1 == 'p' and p2=='s'):
#     print('player 2 wins')
# elif (p1 == 's' and p2=='p'):
#     print('player 1 wins')
# elif (p1 == 's' and p2=='r'):
#     print('player 2 wins')
# elif (p1 == 'r' and p2=='s'):
#     print('player 1 wins')
# elif (p1 == p2): #p p r r s s
#     print('It is a Tie')
# else:
#     print('Invalid Input')

# input a number as integer
# even or odd
# n % 2 == 0 condition

# n = int(input('Enter a no: '))
# if n%2 == 0:
#     print('Even')
# else:
#     print('Odd')

# n = [11,12,13,14]
# for i in n:
#     print(i)
# print('abc')

# n = [11,12,13,14,15,16,17,18]
# for i in n:
#     if (i % 2 == 0):
#         print(f"{i} is Even")
#     else:
#         print(f"{i} is Odd")

# s = 'Python Programming'
# for each in s:
#     print(each)

# paragraph = input('Enter Paragraph: ').split()
# # print(paragraph)
# for each_word in paragraph:
#     print(each_word)

# for i in range(15): #[0,1,2,3,4,....9]
#     print(i,'abcd')
#
# for i in range(5,15): #[0,1,2,3,4,....9]
#     print(i,'abcd')

# Acronym generator
# US -> United States
# step 1 split
# step 2 string access the first letter
# step 3 concat all of these and store in ans variable

# text = input('Enter the abbreviated text: ')
# words = text.split()
# ans = ''
# for each_word in words:
#     ans += each_word[0]
# print(f"The acronym for {text} is {ans}")

# f string, for loop, range
# 1 X 5 = 5
# 2 X 5 = 10
# ...
# table_no = int(input('Enter the table no: '))
# for i in range(1,11):
#     print(f"{i} X {table_no} = {i*table_no}")

# import example_package
# from example_package import module1

# import random
# coins_sides = ['Head','Tail']
# toss_output = random.choice(coins_sides)
# print(toss_output)

import random
# game_inputs = ['r','p','s']
# p1 = input('Enter Rock(r) or Paper(p) or Scissors(s)').lower()[0]
# p2 = random.choice(game_inputs)
# print(f"Computer chose {p2}")
#
# if (p1 == 'r' and p2=='p'):
#     print('Computer wins')
# elif (p1 == 'p' and p2=='r'):
#     print('Human player wins')
# elif (p1 == 'p' and p2=='s'):
#     print('Computer wins')
# elif (p1 == 's' and p2=='p'):
#     print('Human player wins')
# elif (p1 == 's' and p2=='r'):
#     print('Computer wins')
# elif (p1 == 'r' and p2=='s'):
#     print('Human player wins')
# elif (p1 == p2): #p p r r s s
#     print('It is a Tie')
# else:
#     print('Invalid Input')

# i = 1
# while(i < 10):
#     print(i)
#     i += 1 #i+1 -> i

# saved_password = 'pass123'
# user_password = ''
# while ( saved_password != user_password):
#     user_password = input('Enter the password: ')
#     if (user_password == saved_password):
#         print('Success')
#     else:
#         print('Fail,Try again')


# Nested
# if 5>3:
#     if 10 > 5:
#         print()

# x = ['12345',[1,2,3,4,5]]
# for i in x:
#     for j in i:
#         print(j)

# * * *
# * * *
# * * *

# for i in range(5):
#     for j in range(5):
#         print('* ',end = '')
#     print()

# *
# **
# ***
# ****
# *****

# for i in range(5):
#     for j in range(i+1): # 1 2 3 4 5
#         print('* ',end = '')
#     print()

# *****
# ****
# ***
# **
# *

# saved_password = 'pass123'
# count = 0
# while (True):
#     user_password = input('Enter the password: ')
#     if (user_password == saved_password):
#         print('Success')
#         break
#     else:
#         if 'pass' in user_password:
#             print('Your password is semi correct')
#             continue
#         count += 1
#         if count == 3:
#             print('You have exceeded the given attempts')
#             break
#         else:
#             print('Fail,Try again')

# i = 0
# while (i < 10):
#     i += 1
#     if i == 4:
#         # break
#         continue
#     print(i)
#     print(i,i**i)

def pattern():
    n = int(input('Enter a number for pattern: '))
    for i in range(n):
        for j in range(n-i-1): #0 1 2 3 4
            print(' ',end='')
        for j in range(i+1): # 1 2 3 4 5
            print('* ',end = '')
        print()

#   *
#  * *
# * * *

# pattern()
# print(pattern())

# def func():
#     pass
# func()
#
# if (5>3):
#     pass


# Type 2 no argument but return value
# def pattern2():
#     n = int(input('Enter a number for pattern: '))
#     for i in range(n):
#         for j in range(i+1): # 1 2 3 4 5
#             print(i+1,end = '')
#         print()
#     return "Success"
#
# print(pattern2())
# pattern2()

# Type 3 no return but gets an argument
# def pattern3(n):
#
#     for i in range(n):
#         for j in range(i+1): # 1 2 3 4 5
#             print(n-i,end = '')
#         print()
#
# a = 10 #int(input('Enter a number for pattern: '))
# pattern3(a) #pass by referance

# return and argument
# def pattern4(n):
#     for i in range(n):
#         for j in range(n-i):
#             print(' ',end='')
#         for j in range(i+1): # 1 2 3 4 5
#             print(n-i,end = '')
#         print()
#     return n
#
# print(pattern4(6)) #pass by value


# def add():
#     a = int(input('a='))
#     b = int(input('b='))
#     print(f"Addition of {a} and {b} is {a+b}\n")
#
# def sub():
#     a = int(input('a='))
#     b = int(input('b='))
#     return (f"Subtraction of {a} and {b} is {a-b}\n")
#
# def mul(a,b):
#     print(f"Multiplication of {a} and {b} is {a*b}\n")
#
# def div(a,b):
#     return (f"Division of {a} and {b} is {a/b}\n")
#
# print('Welcome to my calculator application')
# while(True):
#     user_option = int(input("1.add\n2.sub\n3.mul\n4.div\nur choice: "))
#     if (user_option == 1):
#         print('You chose addition')
#         add()
#     elif (user_option == 2):
#         print('You chose Subtraction')
#         print(sub())
#     elif (user_option == 3):
#         print('You chose multiplication')
#         a = int(input('a='))
#         b = int(input('b='))
#         mul(a,b)
#     elif (user_option == 4):
#         print('You chose Division')
#         a = int(input('a='))
#         b = int(input('b='))
#         print(div(a,b))
#     else:
#         print('invalid option')

# f = open('varsha-smruti-logee.txt','w')
# f.write("Hi all")
# f.write('Welcome to Pycharm')
# f.close()
#
# f = open('varsha-smruti-logee.txt','a')
# f.write(" more content here")
# f.close()
#
# f = open('varsha-smruti-logee.txt')
# print(f.read())
# f.close()

#create a new file as 'file_operation.py'
# file_name = input('Enter the name of the file: ')
# self_intro = input('Say something about yourself: ')
# f = open(file_name,'w')
# f.write(self_intro)
# f.close()
#
# f = open(file_name)
# print(f"We have successfully written the below content in the file {file_name} "
#       f"\n {self_intro}")

# my_dict = {'name':'Python'}
# print(my_dict['name'])
# print(my_dict['names'])

# my_list = [54,67,89,45,23]
# my_list.remove(45)
# print(my_list)
# my_list.remove(45)

# my_list.delete(67)

# print(var)

# print(12+'15')

# try:
#     file_name = input('Enter the file name: ')
#     f = open(file_name)
# except FileNotFoundError:
#     print('File deleted')
# except NameError:
#     print('Variable Error occured')

# class AgeError(Exception):
#     pass
#
# try:
#     age = int(input('Enter age: '))
#     if age < 0 or age > 100:
#         raise AgeError
#     yob = 2024 - age
#     print(f'You were born in {yob}')
# except AgeError:
#     print('Age should only be between 0 and 100')


# import re
#
# s = input('Enter: ')
# search = input('Pattern: ')
#
# found = re.search(search,s)
# print(f'{search} is present in the string {s} '
#       f'at the index {found.start()}')

# class example:
#     def func(self):
#         self.name = input('Enter name: ')
#         print(f'Hii {self.name} from class')
#
# obj = example() #instatiation
# obj.func()
#
# obj1 = example()
# obj1.func()
#
# print(obj.name)


# class example2:
#     def func1(self,owner):
#         self.name = owner
#
# obj3 = example2()
# obj3.func1('varsha')
# print(obj3.name)

# class constructor:
#     def __init__(self,door_no):
#         self.owner = input('Owner: ')
#         self.door_no = door_no
#
# obj_const = constructor(500)
# print(obj_const.owner)
# print(obj_const.door_no)

# Single Inheritance
class Parent:
    def __init__(self):
        print('From Parent class')
class Child(Parent):
    def __init__(self):
        print('From Child class')
    Parent()
x=Child()

