# Operators 7
# a+b
# + -> operator
# a,b -> operands

# Arithmetic
# + - *
a = 100 #persons
b = 15 #rooms
# print(a+b) #addition
# x = 'Python'
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

n = 5
for i in range(n):
    if ((i == 0) | (i == n-1)):
        for j in range(n):
            print('* ',end='')
    else:
        print('* ',end='')
        for j in range(n-2):
            print('  ',end='')
        print('*',end='')
    print()

