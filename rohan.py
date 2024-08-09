# Operators 7
# a+b
# + -> operator
# a,b -> operands

# Arithmetic
# + - *
a = 100 #persons
b = 15 #rooms
# print(a+b) #addition
# x = 'Completed Python Sessions'
# y = 'Programming'
# print(x+y) #concatenation
# print(a-b)
# print(a*b)
#
# # Division
# print(a/b)
# # Floor division
# print(a//b)
# # Modulus
# print(a % b)
# # Exponentiation
# print(a**b) #100*100*100....

# Comparison or Relational
# a>b -> True False

# >
# <
# >=
# <=
# ==
# !=

# Identity
# is -> ==
# is not -> !=
# a is b

# Assignment
# a = 10
# Augmented assignment operators
# +=
# -=
# *=
# a += 5 # a+5 -> 15 a=15
# print(a)

# Logical operators or Boolean
# T/F 1/0
# print(True and True) #(1*1)
# print(True and False)
# print(False and True)
# print(False and False)

# print(5>3 and 5>4) use case of logical operator

# or (addition)
# print(True or True) #(1+1)
# print(True or False)
# print(False or True)
# print(False or False)

# not
# not True
# not False

# Membership
# x in y
# x not in y

# Flow
# Conditional statement
# loops
# functions

# Conditional statements
# if condition:
#     Statement #indentation
#     Statement
# elif condition:
#     statement
# elif condition
#     statement
# .
# .
# else:
#     statement

# if
#     ---

# if
#     ---
# else
#     ----

# if
#     ---
# elif
#     ---
# .

# age = int(input('Enter ur age: '))
# if (age < 5):
#     print('KG')
# elif ( age < 10):
#     print('Primary')

# While loop

# i = 1
# while (i < 10):
#     print(i)
#     i += 1

# declare a var to store password
# declare another to get the user input
# var1 and var same success
# if not failure


# password = 'pass123'
#
# while(True):
#     user_input = input('Enter password: ')
#     if user_input == password:
#         print('Success')
#         break
#     else:
#         print('Fail')

# Number guessing program
# import random
# print('Welcome to my Number guessing game')
# chosen_number = random.randint(1,100)
#
# user_input = ''
# while(chosen_number != user_input):
#     user_input = int(input('Enter the number: '))
#     if (user_input > chosen_number):
#         print('please choose a smaller no')
#     elif (user_input < chosen_number):
#         print('please choose a bigger no')
#     else:
#         print(f'You found the number {user_input}')
# a= True
# while(a):
#
#     a = False

# i = 1
# while ( i < 10):
#     if i == 4:
#         break
#     print(i)
#     i+=1

# i = 0
# while ( i < 10):
#     i+=1
#     if i == 4:
#         continue
#     print(i) #labeling

# x = [[1,2,3],[4,5,6],[7,8,9]]
 #    0       1       2       Row number
 # 0 1 2    0 1 2   0 1 2     Col number
# 1 2 3
# 4 5 6
# 7 8 9
# for row in x:
#     for col in row:
#         print(col)

# for row in range(3):
#     for col in range(3):
#         print(row,col,end=' | ')
#     print()
#
# for row in range(3):
#     for col in range(3):
#         print('* ',end='')
#     print()

# * * *
# * * *
# * * *

# *
# * *
# * * *

# n = 10
# for row in range(n):
#     for col in range(row+1): #1 2 3
#         print('* ',end='')
#     print()

#    *
#   * *
#  * * *
# * * * *

# n = 5
# for row in range(n):
#     for col in range(n-row-1):
#         print(' ',end='')
#     for col in range(row+1): #1 2 3
#         print('* ',end='')
#     print()

# * * * *
# *     *
# *     *
# * * * *

# n = 5
# for i in range(n):
#     if ((i == 0) | (i == n-1)):
#         for j in range(n):
#             print('* ',end='')
#     else:
#         print('* ',end='')
#         for j in range(n-2):
#             print('  ',end='')
#         print('*',end='')
#     print()

# def searchTask(task):
#     if task in list_of_tasks:
#         return True
#     return False
# def addTask(task):
#     if not searchTask(task):
#         list_of_tasks.append(task)
#         return "Task added Successfully"
#     return "Task is a Duplicate"
#
# def removeTask(task):
#     if searchTask(task):
#         list_of_tasks.remove(task)
#         return "Task Removed Successfully"
#     return "Task not found"
#
#
#
# print('Welcome to my task manager application')
# list_of_tasks = []
# while(True):
#     user_option = input('\nChoose an option from below\n'
#                         'Add\n'
#                         'Remove\n'
#                         'Search\n'
#                         'NumTasks\n'
#                         'Tasks\n'
#                         'Option: ').lower() #ADD Add add
#     if (user_option == 'add'):
#         task = input('Enter the name of the task to be added: ').lower()
#         print(addTask(task))
#     elif (user_option == 'remove'):
#         task = input('Enter the name of the task to be removed: ').lower()
#         print(removeTask(task))
#     elif (user_option == 'search'):
#         task = input('Enter the name of the task to be searched: ').lower()
#         if searchTask(task):
#             print('Task found')
#         else:
#             print('Task not found')
#     elif (user_option == 'numtasks'):
#         print(f"There are {len(list_of_tasks)} tasks to be done\n")
#     elif (user_option == 'tasks'):
#         print('\nAvailable tasks are')
#         for each_task in list_of_tasks:
#             print(f"-> {each_task}")

# Calculator.py

# def add(): #type 1
#     a = int(input('a='))
#     b = int(input('b='))
#     add = a+b
#     print(f'Addition of {a} and {b} is {add}')
# def sub(): #type 2
#     a = int(input('a='))
#     b = int(input('b='))
#     sub = a - b
#     return (f'Subtraction of {a} and {b} is {sub}')
# def mul(a,b): #type 3
#     mul = a * b
#     print(f'Multiplication of {a} and {b} is {mul}')
# def div(a,b): #type 4
#     div = a / b
#     return (f'Multiplication of {a} and {b} is {div}')

# print('Welcome to my calculator app')
# while True:
#     options = input('Choose an Operation to carry (+,-,*,/): ')
#     if options == '+':
#         add()
#     elif options == '-':
#         print(sub())
#     elif options =='*':
#         a = int(input('a='))
#         b = int(input('b='))
#         mul(a,b)
#     elif options == '/':
#         a = int(input('a='))
#         b = int(input('b='))
#         print(div(a,b))
#     else:
#         print("Thank you")
#         break

# open
# close
# read
# write

# open
# filename
# processing mode 4+2
# file = open('rohan.txt','w')
# file = open('rohan.txt','x')
# file = open('rohan.txt','a')

# close

# f = open('rohan.txt')
#
# f.close()
# f = open('rohan.txt','w')
# f.write("HI my name is Rohan")
# f.close()

# f = open('rohan_python.txt','x')
# f.write("Hi my name is Rohan and I'm learning python")
# f.close()

# f = open('rohan.txt','a')
# f.write(" I am learning python")
# f.close()

# f = open('rohan.txt')
# print(f.read())

# RegEx - Regular Expressions

# String
# email - svr@mail.com
#         svr
#         @
#         mail
# .
# com

import re

# s = "Hello all welcome to the malleable"
# file = open("dakbooeni.txt")
# s = file.read()
# print(s)
# res = re.findall('python',s)
# print(res)
# res = re.search('all',s)
# print(res.start())
# print(res.end())
# res = re.split('all',s)
# print(res)
# new_s = re.sub('all','---',s)
# print(new_s)

# s = "Hello Heado Healo"
# res = re.findall('He..o',s)
# print(res)

# print(rohan)
# rohan = 235
# rohan = [1,2,3]
# try:
#     rohan.remove(5)
# except NameError:
#     print('variable is not defined')
# except ValueError:
#     print('Value not found')

# class AgeError(Exception):
#     pass
# while True:
#     age = int(input('Enter your age: '))
#     current_year = 2024
#     try:
#         if age<0:
#             raise AgeError
#         YOB = current_year - age
#         print(f'You were born in {YOB}')
#     except AgeError:
#         print('Enter an appropriate age')

class example:
    owner = ''
    def func(self):
        self.owner=input('Enter owner name: ')
        print(self.owner)

example_object = example() #creating an instance
# example_object.owner = 'Rohan'
example_object.func()

class example:
    def __init__(self): #constructor
        self.owner=input('Enter owner name: ')
        print(self.owner)

example_object = example() #creating an instance
