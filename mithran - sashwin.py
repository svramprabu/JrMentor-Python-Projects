# for iterating_var in sequence:
#     Statement


# paragraph = input('Enter / Paste the para here: ')
# words = paragraph.split()
# n = 0
# for each_word in words:
#     n += 1 #n+1
# print(f"Number of words present in the paragraph is {n}")

# Acronym Generator using for loop
# United Nations UN
# United States US
# Indian Space Research Organization ISRO

# user_input = input('Enter here: ')
# words = user_input.split()
# ans = ''
# for each_word in words:
#     ans += each_word[0].upper() #I S R O
# print(f"Acronym for {user_input} is {ans}")

# nums = [12,23,3456,34,67]
#
# for each_num in nums:
#     if (each_num % 2 == 0):
#         print(f"{each_num} is an even number")
#     else:
#         print(f"{each_num} is an odd number")

# s = "Completed Python Sessions Programming"
# for ch in s:
#     print(ch)

# s = input("enter string: ")
# ltr = input('enter letter: ')
# answer = 0
# for ch in s:
#     if (ch == ltr):
#         answer += 1
# print(f"Number of times {ltr} occured in {s} is {answer}")

# s = input('enter string: ') #environment -> enviromt
# answer = ''
# for ch in s:
#     if (ch.lower() not in answer):
#         answer += ch.lower()
# print(f"Before: {s}")
# print(f"After: {answer}")

# s = input('Enter string: ')
# vowels = "aeiou"
# ans = 0
# for ch in s:
#     if (ch.lower() in vowels):
#         ans += 1
# print(f"Number of vowels in {s} is {ans}")

# for i in range(10):
#     print(i)
#
# for i in range(1,20):
#     print(i)
#
# a = 10
# b = 50
# for i in range(a,b):
#     print(i)

# 1 x 2 = 2
# 2 x 2 = 4
# 3 x 2 = 6

# n = int(input('Enter table_no: '))
# for i in range(1,11):
#     print(f"{i} X {n} = {i*n}")

# 1 | 2 | 3
# 4 | 5 | 6
# 7 | 8 | 9

# x = [1,2,3,4,5,6,7,8,9]
# for el in x:
#     print(el)

# y = [[1,2,3],[4,5,6],[7,8,9]]
# for row in y:
#     print(row)

# y = [[1,2,3],[4,5,6],[7,8,9]]
# for row in range(3):
#     for el in range(3):
#         print('* ',end="")
#     print()

# n = int(input('Enter a no: '))
# for i in range(n):
#     for j in range(n):
#         print('* ',end="")
#     print()

# *
# * *
# * * *


# n = int(input('Enter a no: '))
# for i in range(n): #rows
#     for j in range(i+1): #col 1 2 3
#         print('* ',end="")
#     print()

# for i in range(3):
#     print(i+1)

# * * *
# * *
# *
# n = 3
# for i in range(n):
#     print(n-i)

# n = int(input('Enter a no: '))
# for i in range(n): #rows
#     for j in range(n-i): #col
#         print('* ',end="")
#     print()

# n = int(input('Enter a no: '))
# for i in range(n): #rows
#     for j in range(i+1): #col 1 2 3
#         print(i+1,end="")
#     print()

# 1 2 3
# 1 2
# 1

# while condition:
#     statement

# i = 0
# while (i<10):
#     print(i)
#     i += 1
# print('End of while')

# i = 0
# while (i<100):
#     i += 5
#     if (i % 2 == 0):
#         print(f"{i} is even")
#     else:
#         print(f"{i} is odd")

# num = int(input('Enter a number: ')) #12345
# add = 0
# digits = 0
# for each in str(num): #'12345' 1 2 3 4 5
#     add += int(each)
#     digits += 1
#
# print(f'Sum of digits of {num} is {add}')
# print(f'Number of digits of {num} is {digits}')

# num = int(input('Enter a number: ')) #12345
# n = num
# add = 0
# digits = 0
# while(n>0): #12345 -> 1234 5 -> 123 4 -> 12 3
#     last_digit = n % 10 #5 4 3 2 1
#     add += last_digit
#     n = n // 10 #1234 123 12 1 0
#     digits += 1
# print(f'Sum of digits of {num} is {add}')
# print(f'Number of digits of {num} is {digits}')

# saved_password = 'pass123'
# user_password = input('Enter password: ')
# while(user_password != saved_password):
#     if (user_password == saved_password):
#         print('Success')
#     else:
#         print('Fail')
#         user_password = input('Enter again: ')
# print('You have entered the right password')

# import random
# chosen_number = random.randint(1,100)
# user_number = int(input('Enter no: '))
# while(user_number != chosen_number):
#     if user_number > chosen_number:
#         user_number = int(input('Enter a smaller no: '))
#     elif user_number < chosen_number:
#         user_number = int(input('Enter a bigger no: '))
# print('Thank you for playing and you found the number')

# Break and Continue
# i = 0
# while (i<10):
#     i += 1
#     if (i == 4):
#         # break
#         continue
#     print(i)

# saved_password = 'pass123'
# while(True):
#     user_password = input('Enter password: ')
#     if (user_password == saved_password):
#         print('Success')
#         break
#     else:
#         if 'pass' in user_password:
#             print('Semi correct')
#             continue
#         print('Fail')
# print('You have entered the right password')

# taskmanager.py

# print('Welcome to my task manager app')
# list_of_task = []
# while(True):
#     user_option = int(input('\n1.Add a task'
#                             '\n2.Remove a task'
#                             '\n3.Search a task'
#                             '\n4.Number of Tasks'
#                             '\n5.Print tasks'
#                             '\nEnter option:'))
#     if (user_option == 1):
#         print("You chose to add a task")
#         task = input('Enter task name: ')
#         if task not in list_of_task:
#             list_of_task.append(task)
#             print('Task addded successfully')
#         else:
#             print('Task already present')
#     elif (user_option == 2):
#         print("You chose to remove a task")
#         task = input('Enter task name: ')
#         if task not in list_of_task:
#             print('Task not found')
#         else:
#             list_of_task.remove(task)
#             print('Task removed successfully')
#     elif (user_option == 3):
#         print("Let's search for a task")
#         task = input('Enter task name: ')
#         if task in list_of_task:
#             print("Task found")
#         else:
#             print("Task not found")
#     elif (user_option == 4):
#         n = len(list_of_task)
#         print(f"The number tasks available are {n}")
#     elif (user_option == 5):
#         print('\nAvailable tasks are')
#         for each in list_of_task:
#             print(f"-> {each}")


# Functions
# Type 1
# def car():
#     print('bmw')
# car()
# print(car())

# Type 2
# def bus():
#     return 'Minibus'
# print(bus())
# b = bus()
# print(b)

# Type 3
# def taxi(passengers):
#     print(f'We have {passengers} seats in the taxi')
# taxi(7)

# Type 4
# def train(seat):
#     return seat
# print(train('D15'))

# calculator.py

# def add(): #type 1
#     a = int(input('a='))
#     b = int(input('b='))
#     add = a + b
#     print(f"Addition of {a} and {b} is {add}")
# def sub(): #type 2
#     a = int(input('a='))
#     b = int(input('b='))
#     sub = a - b
#     return f"Subtraction of {a} and {b} is {sub}"
# def mul(x,y): #type 3
#     mul = x * y
#     print(f"Multiplication of {a} and {b} is {mul}")
# def div(x,y): #type 4
#     pass
# print('Welcome to my calculator program')
# while True:
#     option = input('+ - * / \nchoose one option:')
#     if option == '+':
#         print('Addition')
#         add()
#     elif option =='-':
#         print('Subtraction')
#         print(sub())
#     elif option == '*':
#         print('Multiplication')
#         a = int(input('a='))
#         b = int(input('b='))
#         mul(a,b)

# file operations
# open
# close
# read
# write

# file = open('filename.extention','processing mode')
# processing modes 6 -> 4+2
# r read only mode - default
# file = open('sashmithran.txt','r')
# file = open('sashmithran.txt')
# w write - create / truncate
# file = open('sashmithran.txt','w')
# x exclusive creation /error
# file = open('sashmithran.txt','x')
# a - append create / not truncate
# file = open('sashmithran.txt','a')
# t - text mode - default
# b - binary mode
# file = open('sashmithran.txt','x+b')

# close operation
# file = open('sashmithran.txt')
#
# file.close()

# file = open('sashmithran.txt','w')
# file.write("Hi from Python class")
# file.close()
# file = open('sashmithran.txt')
# print(file.read())
# file.close()

# file = open('sashmithran.txt','x')
# file.write("Hi from Python class")
# file.close()
# file = open('sashmithran.txt')
# print(file.read())
# file.close()

# file = open('sashmithran.txt','a')
# file.write(" doing file operations")
# file.close()
# file = open('sashmithran.txt')
# print(file.read())
# file.close()

# Regular Expressions - RegEx
# svr@mail.com
# import re
# s = "Hello all welcome home ball mall call malleable"
# result = re.findall('all',s)
# print(result)
# result = re.search('all',s)
# print(result.start())
# print(result.end())

# import re
# s = "Hello all welcome home ball mall call malleable"
# split_result = re.split('all',s)
# print(split_result)
#
# sub_s = re.sub(' ','---',s)
# print(sub_s)

# print(mithran) #NameError
# print(15+'10')
# my_list =[1,2,3]
# print(my_list[5])
# my_list.remove(10)
# my_list.removes(10)

# try:
#     print(mithran)
# except NameError:
#     print("Variable not defined")
#
# try:
#     print(15+'10')
# except TypeError:
#     print("Type error occured")
#
# try:
#     my_list =[1,2,3]
    # print(my_list[5])
    # my_list.remove(10)
    # my_list.removes(10)
#     print(13+'6')
# except IndexError:
#     print("Index not in range")
# except ValueError:
#     print("Value not found")
# except AttributeError:
#     print("Attrtribute spelled wrong")

class AgeError(Exception):
    pass

try:
    age = int(input('enter your age: '))
    if age < 0:
        raise AgeError
    current_year = 2024
    birth_year = current_year - age
    print(f"you were born in {birth_year}")
except AgeError:
    print("Enter a positive age")