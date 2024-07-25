# variable_1 = 12345
# print(variable_1)
#
# int_var = 12345
# print(int_var)
# print(type(int_var))
#
# float_var = 99.5
# print(float_var)
# print(type(float_var))
#
# str_var = "Hi and welcome to Day 5!!!"
# print(str_var)
# print(type(str_var))

#H.W: Declare name,age and weight
# name = 'Ramprabu'
# age = 30
# weight = 75.6

# s = "PythonProgramming"
# print(s)

# print(s[index_number])

# PythonProgramming
# 0123456789......

# P -> in "Python" -> 0
# Q -> in "Query" -> 0
# S -> in "test" -> 2
# R -> in "String" -> 2
# I -> in "King" -> 1
#     K - 0
#     i - 1
#     n - 2
#     g - 3

# s = "Python"
# print(s)
# print(s[0])
# print(s[1])
# print(s[4])
#
# name = "Ramprabu"
# print(name[3])

# x = "Roshan"
# print(x[5])
# print(x[-1])
# print(x[-2])

# Comments

# print('An example statement') #type your comment
# print('An example statement') # description
# print('An example statement') # explanation

# name1 = "Ram"
# print(type(name1))
# age1 = 30
# print(type(age1))
#
# name = input('Enter your name: ')
# print(name)
# print(type(name))
#
# age = int(input('Enter your age: '))
# print(age)
# print(type(age))
#
# weight = float(input('Enter your weight: '))
# print(weight)
# print(type(weight))

# a = 10
# b = 20
# c = 30
# print(a)
# print(b)
# print(c)
#
# print(a,b,c)
# print(a,b,c,sep=" ")
# print(a,b,c,sep="--->")
# print(a,sep="--->")

# Arithmetic Operators

# + addition
# x = 15
# y = 20
# print('x+y=',x+y)

# p = 14.5
# q = 15.7
# print('p+q=',p+q)
#
# # + concatenation
# a = 'Python'
# b = 'Program'
# print('a+b=',a+b)

# - Subtraction
# a = 10
# b = 5
# print('a-b=',a-b)

# * Multiplication
# a = 5
# b = 2
# print('a*b=',a*b)
#
# a = 15 #no of chocolates
# b = 4 #children
# # / division
# print('a/b=',a/b,'chocolates per child')

# // floor division
# x = 21 #no of children
# y = 4 #cars
# print('x//y=',x//y,'children per car')

# % modulo
# print('x%y=',x%y,"children without car")

# ** power or exponentiation
# a = 3
# b = 5
# print('3**5=',a**b)
# 3**5 -> 3*3*3*3*3

# Python program to find the cost of apples
# if x plans to buy 8 apples at the price of 17 each

# apples = 8
# price_per_apple = 17
# cost_of_apples = apples * price_per_apple
# print("Cost of 8 apples at 17 each is",cost_of_apples)

# Comparison Operators
# a = 10
# b = 8
# print("Greater than")
# print(f"{a} > {b} = {a>b}")
# print(f"{b} > {a} = {b>a}")
#
# x = 20
# y = 45
# print("Less than")
# print(f"{x} < {y} = {x<y}")
# print(f"{y} < {x} = {y<x}")

# print('less than equals')
# a = 8
# b = 10
# print(f"{a}<={b}={a<=b}")
# a = 10
# b = 10
# print(f"{a}<={b}={a<=b}")
# a = 12
# b = 10
# print(f"{a}<={b}={a<=b}")

# Assignment operators

# a = 10
# Augmented assignment operators

# +=
# -=
# *=
# /=
# //=
# %=
# **=

# a = 5
# print(a)
# a += 10 #a+10 -> 15 -> a=15
# print(a)

# Logical Operators or Boolean Operators
# True / False
# AND -> True only when both are True
# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)
# OR -> False only when both are False
# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)
# NOT ->
# print(not True)
# print(not False)

# print('one')
# print('two')
# print('three')

# Conditional Statements
# if
# elif
# else

# if condition:
#     Statement1
#     Statement2
#     Statement3

# if (5 > 3):
#     print('Five')
#     print('Greater than')
#     print('Three')

# if condition:
#     Statement
# else:
#     Alternative Statement

# a = 10
# b = 8
# if (a > b):
#     print('a is greater than b')
# else:
#     print('a is not greater than b')
# c = 10
# d = 80
# if (c > d):
#     print('c is greater than d')
# else:
#     print('c is not greater than d')

# if condition:
#     Statement
# elif condition1:
#     statement1
# elif condition2:
#     statement2
# .
# .
# .
# else:
#     Alternative Statement

# a = 10
# b = 10
# if (a>b):
#     print('a is greater than b')
# elif (a<b):
#     print('a is less than b')
# else:
#     print('a is equal to b')

# Voting Eligibility
# age = int(input('What is your age? '))
# if (age >= 18):
#     print('You are Eligible to vote')
# else:
#     print('You are not Eligible to Vote')

# day = input('Enter a day in the week: ')
# if (day == 'sunday'):
#     print('It is weekend')
# elif (day == 'saturday'):
#     print('It is weekend')
# else:
#     print("It is a weekday")

age = int(input('Enter age: '))
if age <= 5:
    print('KG')
elif age <= 10:
    print('Primary')
elif age <= 15:
    print('Secondary')
elif age < 18:
    print('Higher Secondary')
else:
    print('Completed school')















































