# kri_shna = 12124 #Declaring a variable
# print(kri_shna)

# eg_str = "Python @123"
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