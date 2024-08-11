# kri_shna = 12124 #Declaring a variable
# print(kri_shna)

# eg_str = "Completed Python Sessions @123"
# print(eg_str)
# print(eg_str[0])
# print(eg_str[3])
# print(eg_str[-1])

# decalre a var
# store all alphabets as strign
# use strign access to print
# just the vowels
# a e i - positive indexing
# o u - negative indexing

# Boolean Datatypes
# x = True
# y = False
# print(type(x))

# eg_list = [[1,2],[3,4]]
# print(eg_list)
# print(eg_list[0])
# print(eg_list[0][0])
#
# [['venkat','father'],['vasanthi','mother']]

# eg_list = [1,2,3,4]
# eg_tuple = (1,2,3,4)
# # print(type(eg_tuple))
# print(eg_list)
# eg_list[2] = 'Krishna'
# print(eg_list) #mutability

# print(eg_tuple[2])
# eg_tuple[2]='Krishna'

# my_list = [4,2,9,6,3]
# print(my_list)
# print(my_list[2])
#
# my_list.sort()
# print(my_list)
# print(my_list[2])

# empty_dict = {}
# print(empty_dict)
#
# int_key_dict = {1:'krish',5:'python'}
# print(int_key_dict)
#
# my_dict = {5:'krish','age':16}
# print(my_dict)
#
# print(my_dict[5])
# print(my_dict['age'])

# chocolates = 14
# children = 4
# choc_per_kid = chocolates / children #division
# print(choc_per_kid)

# children = 14
# rooms = 4
# kid_per_room = children // rooms #floor division
# print(kid_per_room,'kids per room')
# kids_left_without_rooms = children % rooms #modulo
# print(kids_left_without_rooms,'kids left wihtout room')

# a = 5
# print(a)
# a += 13
# print(a)
# a -= 4
# print(a)
# a *= 3
# print(a)
# a /= 4
# print(a)

# Bitwise Operators
# a -> decimal -> binary -> bitwise -> binary -> decimal
# b -> decimal -> binary
# print(10 & 14)
# 0100101010
# 1010101000
# &
# |

# Identity operators
# ==
# is

# !=
# is not

# Membership operators
# x in y
# print(5 in [1,2,3,4])
# x not in y

# age = int(input('Enter your age: '))
# yob = 2024 - age
# if (age > 18):
#     print(f'You are Eligible to Vote as you were born on {yob}')


# age = int(input('Enter your age: '))
# yob = 2024 - age
# if (age > 18):
#     print(f'You are Eligible to Vote as you were born on {yob}')
# else:
#     print("You are not eligible to vote")

# saved_password = "pass123"
# user_password = input("Enter password: ")
# if ( user_password == saved_password):
#     print("Logged in successfully")
# else:
#     print("please enter the correct pwd")

# if condition1:
#     Statement1
# elif con2:
#     Stat2
# elif con3:
#     stat3
# .
# .
# .
# else:
#     Alternative Statements

# days_of_week = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
# user_day = input('Enter your fav day of the week: ').lower()
# if user_day == 'sunday':
#     print('Yeaaa its a fun day')
# elif user_day == 'friday':
#     print('Weekend is here')
# elif user_day == 'monday':
#     print('Are you sure???')
# else:
#     if user_day in days_of_week:
#         print('Yet another day of the week')
#     else:
#         print('Invalid input')

# age = input()
# age below 5 -> kindergarten
# age below 10 -> primary
# age below 15 -> secondary
# age below 18 -> higher secondary

# 3 -> 3^1 -> 3
# 3^2 -> 3*3 -> 9
# r p
# p r
# r s
# s r
# p s
# s p

# print('Welcome to my Rock Paper Scissors Game')
# p1 = input('Choose Rock(r) or Paper(p) or Scissors(s): ').lower()[0]
# p2 = input('Choose Rock(r) or Paper(p) or Scissors(s): ').lower()[0]
#
# if (p1 == 'r' and p2 == 'p'):
#     print('player 2 won')
# elif (p1 == 'p' and p2 == 'r'):
#     print('plauer 1 won')
# elif (p1 == 'p' and p2 == 's'):
#     print('plauer 2 won')
# elif (p1 == 's' and p2 == 'p'):
#     print('plauer 1 won')
# elif (p1 == 's' and p2 == 'r'):
#     print('plauer 2 won')
# elif (p1 == 'r' and p2 == 's'):
#     print('plauer 1 won')
# elif (p1 == p2):
#     print('Its a tie')
# else:
#     print('Invalid input')

# For
# for iterating_variable in sequence:
#     Statements using iterating_variable
# While
# while (condition):
#     Statements

# computer_parts = ['monitor','printer','mice','keyboard']
# for each_part in computer_parts:
#     print(each_part)

# paragraph = input('Enter / paste para: ')
# words = paragraph.split()
# for word in words:
#     print(word)

# Generate Acronym
# United States -> US
# abbr = input('Enter the abbreviated text: ')
# words = abbr.split()
# acro = ''
# for word in words:
#     acro += word[0].upper()
# print(f"Acronym for {abbr} is {acro}")

# s = "Krishna"
# for i in s:
#     print(i)

# s = input('Enter: ')
# reverse_s = ''
# for each_char in s:
#     reverse_s = each_char + reverse_s
# print(f"Reverse of {s} is {reverse_s}")

# s = input('Enter: ')
# letters = 0
# digits = 0
# for i in s:
#     if i.isdigit():
#         digits += 1
#     elif i.isalpha():
#         letters += 1
# print(f'Number of digits is {digits}\n'
#       f'Number of Letters is {letters}')

# range(10) -> 0-9
# range(15) -> 0-14
# range(3,15) -> 3-14

# for num in range(20):
#     print(num)
#
# for num in range(1,20):
#     print(num)

# 1 x 5 = 5
# 2 x 5 = 10
# 3 x 5 = 15
# .
# .

# table_no = int(input('Enter table number: '))
# for i in range(1,13):
#     print(f"{i} x {table_no} = {i*table_no}")

# my_list = ['apple','ball','cat','dog','elephant']
# my_list[0]
# my_list[1]
# my_list[2]
# l=len(my_list)
# for i in range(l):
#     print(my_list[i])

# 12345
# 5
# 1+2+3+4+5
# num = int(input('Enter a number: '))
# d = 0
# s = 0 #int
# str_num = str(num)
# d = len(str_num)
# for each_d in str_num:
#     s += int(each_d) #str
# print(f"sum of {num} is {s}")
# print(f"Number of digits in {num} is {d}")

# while condition:
#     statement

# i = 0
# while i<10:
#     print(i) #statement
#     i += 1 #i = i+1

# num = 12341553
# # print(num % 10)
# # print(num // 10)
# s,d=0,0
# n = num
# while (n > 0):
#     last_digit = n % 10
#     d += 1
#     s += last_digit
#     n //= 10 #n = n//10
# print(f"sum of {num} is {s}")
# print(f"Number of digits in {num} is {d}")

# saved_password = 'pass123'
# user_password = input('Enter password: ')
# while (user_password != saved_password):
#     if user_password!= saved_password:
#         print('Try again')
#         user_password = input('Enter password again: ')
#     else:
#         print('success')

# Armstrong number
# 123
# 1^3 + 2^3 + 3^3 = 123

# number = int(input('Number: '))
# n = number
# s = 0
# while (n>0):
#     ld = n % 10
#     s += (ld ** 3)
#     n //= 10
# if number == s:
#     print('It is an Armstrong number')
# else:
#     print("Not an Armstrong number")

# i=0
# while (i<10):
#     i+=1
#     if (i % 5 == 0):
#         break
#     print(i)

# saved_pass = "pass123"
# attempt = 0
# while True:
#     user_pass = input('Enter pwd: ')
#     if user_pass != saved_pass:
#         if attempt == 2:
#             print('Your attempts are over')
#             break
#         attempt += 1
#         print(f'You are left with {3-attempt}')
#         print("Try again")
#     else:
#         print("success")
#         break

# i = 0
# while i<10:
#     i+=1
#     if (i % 5 == 0):
#         continue
#     print(i)

# saved_pass = "pass123"
# attempt = 0
# while True:
#     user_pass = input('Enter pwd: ')
#     if user_pass != saved_pass:
#         if attempt == 2:
#             print('Your attempts are over')
#             break
#         elif 'pass' in user_pass:
#             print('semi correct')
#             continue
#         attempt += 1
#         print(f'You are left with {3-attempt}')
#         print("Try again")
#     else:
#         print("success")
#         break

# my_list = ['Python','Java']
# for each in my_list:
#     for ch in each:
#         print(ch)

# 0 0 1 2
# 1 0 1 2
# 2 0 1 2

# n = 3 #no of rows as well as no of colums
# for row in range(n):
#     for col in range(n):
#         print(f"{row}{col}",end=" ")
#     print()

# def func1():
#     print('abc')
#     print(123)
#
# func1()
#
# def func2():
#     c = 5+3
#     return True
#
# add = func2()
# print(add)
# print(func2())

# name = input('name?')

# def func3(a):
#     print(a)
#
# c = 10
# func3(c) #pass by ref
# func3(13) #pass by value
#
# def func4(a,b):
#     c = a+b
#     return c
#
# add = func4(4,5)
# print(add)


















