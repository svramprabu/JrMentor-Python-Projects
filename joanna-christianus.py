# Declaring or Assigning a variable
# variable_name = Data
# a = 12344

# Printing a variable
# print(variable_name)
# print(a)

# int - 0,1,2,3,....-1,-2,-3...
# float - 1.34,5.97,...-4.567,767.8645,...

# abc = 2344234
# efg = 3242.66546
# question = "What is your name?" #to explain string data type
# str1="123456"

# print(abc)
# print(efg)
# print(question)
# print(type(abc))
# print(type(efg))
# print(type(question))

# String access
# test_string = 'Hello World'
# print(test_string)
# print(test_string[0])
# print(test_string[6])

# x = 10 #int
# y = 15.5 #float
# add = x + y #int + float
# print(add) # returns 25.5 due to implicit type conversion

# Explicit type conversion or Typecasting

# Inbuilt functions
# int()
# float()
# str()

# example
# x = 10 #int
# y = '5' #str
# y = int(y) #type casting and storing it back in y
# add = x + y
# print(add)

# x = 'Hackerkid'
# print(x)
# a = input('Enter your name') #example of input function
# print(a)

# name = input('Enter your name')
# age = int(input('Enter your age'))
# weight = float(input('Enter your weight'))
# print(name,age,weight)

# print(5,6,7,8,9,sep='^^^',end='--->')
# print(456) # 5^^^6^^^7^^^8^^^9--->456

# 123$$$456$$$789===>12345

# to print both string and var
# a = 10
# print(a) #10
# print('hi everyone') #hi everyone
# # method 1
# print(a,'hi everyone') #10 hi everyone
# n = 'christinaus'
# print('hi',n) #hi christianus
# # method 2
# print(f"Hi {n} ") #Hi christianus

# name = input('Name: ')
# age = int(input('Age: '))
# weight=float(input('Weight: '))
# print(f" My name is {name} and I am {age} years old weighing {weight}")

# Arithmetic operators
# Mathematical calculations and operations
# Input - 2 data -> 2 numbers
# Output - 1 data -> 1 number

# + -> addition
# print(5 + 3)

# - -> subtraction
# print(5-3)

# * -> multiplication
# print(5 * 3)

# / -> divition
# print(10 / 2)

# % -> reminder
# print(10 % 3)

# ** -> exponentiation or power
# print(2 ** 3)
# 2 x 2 x 2

# name = input('Your name: ')
# english = int(input('Enter english marks'))
# tamil = int(input('Enter tamil marks'))
# maths = int(input('Enter maths marks'))
#
# total = english + tamil + maths
# print(f'Hi, {name} your total marks is {total}')
# average_marks = total / 3
# print(f'your average marks is {average_marks}')


# > Greater than
# x>y
# x should be bigger than y

# print('20 > 10',20 > 10)
# print('10 > 20',10 > 20)

# < Lesser than
# x < y
# x should be smaller than y

# print('10 < 20',10<20)
# print('20 < 10',20<10)

# == value equals
# x == y
# x is equal to y

# print('10 == 10',10 == 10)
# print('10 == 20',10 == 20)

# != value not equals
# x != y
# x is not equal to y

# print('10 != 20',10 != 20)
# print('10 != 10',10 != 10)

# >= greater or equal to
# x >= y
# x is greater than or equal to y
# print('10 >= 10',10 >= 10)
# print('10 >= 8',10 >= 8)
# print('10 >= 20',10 >= 20)

# <= less than or equal to
# x <= y
# x is less than or equal to y
# print('10 <= 10',10 <= 10)
# print('10 <= 12',10 <= 12)
# print('10 <= 8',10 <= 8)

# a = int(input('a='))
# b = int(input('b='))
#
# print(f'{a}>{b}',a>b)
# print('a<b',a<b)
# print('a==b',a==b)
# print('a!=b',a!=b)
# print('a>=b',a>=b)
# print('a<=b',a<=b)

# import random
# option = int(input('Enter 1 to roll and 2 to exit: '))
# while(option == 1):
#     dice_output = random.randint(1,6)
#     print(f"After rolling the dice you got {dice_output}")
#
#     option = int(input('Enter 1 to roll and 2 to exit'))

# import random
# game_inputs = ['r','p','s']
# computer_choice = random.choice(game_inputs)
# print(computer_choice)

# from package_name import module_name

# def car():
#     print('skdjbf')
# car()
# print(car())

# Type 2:
# def bike():
#     name = 'Yamaha'
#     return name
#
# print(bike())
#
# def train(train_name):
#     print(train_name)
#
# train('Chennai Express') #pass by value
#
# def flight(flight_no):
#     return flight_no
#
# x = 1234
# print(flight(x)) #pass by ref

# def rps(p1,p2):
#     if
#         pr
#
#
# player_mode = input('single/double')
#
# if single
#     import
#     computer
#     player
#     rps(comuter,player)
# else
#     p1
#     p2
#     rps(p1,p2)


# f = open('sample.txt','w')
# with open('sample.txt','a') as f:
#     f.write('Type not here')

class car:
    print('BMW')

# a = car()

# OOPS
# Inheritance
# Abstraction
# Encapsulation
# Polymorphism