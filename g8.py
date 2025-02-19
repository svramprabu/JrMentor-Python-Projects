# for
# if
# while
# global
# break
# continue
# from traceback import print_tb
from re import fullmatch

# Identifier
# name anything as per our will
# Rules in naming
# python

# abc = 12345
# print(abc)
# defg = 456
# print(defg)
# klm = 123414
# print(klm)

# var_one = 23424
# print(var_one)
# print(type(var_one))
#
# var_two = 234.345
# print(var_two)
# print(type(var_two))
#
# var_t = True
# print(var_t)
# print(type(var_t))
#
# var_f = False
# print(var_f)
# print(type(var_f))
#
# s = 'python123@mail.com'
# print(s)
# print(type(s))
#
# s1 = '123124'
# print(s1)
# print(type(s1))

# s_1 = ''
# s_2 = ';'
# s_3 = 'sjkbdi2743y@$T'

# s = "HackerKid"
# print(s)
# print(s[0])
# print(s[5])
# print(s[8])

# print(s[-1])
# print(s[-3])
# print(s[-9])

# declare a variable and store alphabets
# print vowels a,e,i,o,u

# Hackerkid
# String Slicing
# print(s[start:stop])
# s = "HackerKid"
# print(s[3:7])
# print(s[3:])
# print(s[:7])
# print(s[:])

# print(s[start:stop:step=1])
# s = "hippopotamus"
# print(s[2:9])
# print(s[2:9:1])
# print(s[2:9:2])
#
# print(s[:-1])
# print(s[-1:])
# print(s[-1::-1])
# print(s[::-1])

# declare a variable and
# programming
# gram

# s = "pyThOn prograMMING"
# print(s.upper())
# print(s)
# print(s.lower())
# print(s.title())
# print(s.capitalize())

# s = "pyThOn prograMMING"
# print(s)
# print(s.swapcase())
# print(s.islower())
# print(s.isupper())

# s = "pyThOnprograMMING"
# n = "12345"
# print(n.isdigit())
# print(s.isdigit())
# print(s.isalpha())
# print(n.isalpha())

# s = "    Hacker     kid    "
# print(s)
# print(s.strip())
# print(s.lstrip())
# print(s.rstrip())

# s = "Hi my name is ram and ram i teach python"
# print(s.find('ram'))
# print(s.rfind('ram'))
# print(s.replace('ram','Ram'))
# print(s)

# s = "Hi my name is ram and ram i teach python"
# print(s)
# print(s.split())
# print(s.split('and'))
# s = 'ram,30,mdu'
# print(s.split(','))

# List, Tuple, Dictionary
# [],(),{}
# store multiple datas
# List & Tuple
# Ordered sequence of values

# deer -> animal
# reed -?

# 1,2,3,4 -> values
# [1,2,3,4] -> list
# (1,2,3,4) -> tuple

# values made of int - type 1
# int_list = [1,2,3,4,5]
# print(int_list)
# int_tuple = (1,2,3,4,5)
# print(int_tuple)

# values made of strings type 2
# str_list = ['kaushik','prativ','sherina','rudransh']
# print(str_list)
# str_tuple = ('kaushik','prativ','sherina','rudransh')
# print(str_tuple)

#no values type 3
# empty_list = []
# print(empty_list)
# empty_tuple = ()
# print(empty_tuple)

# mixed values type 4
# mixed_list = [123,234.45643,'python']
# print(mixed_list)
# mixed_tuple = (123,234.45643,'python')
# print(mixed_tuple)

# nested_list = [[1,2],[3,4],[5,6,7]]
# print(nested_list)

# []
# ()

# Mutability - ability to change a single value
# List Mutable
# Tuple Immutable

# my_list = ['Kaushik','Prativ','Sherina','Rudransh']
# print(my_list)
# print(my_list[1])
# my_list[1]='Prativ Ram'
# print(my_list)

# my_tuple = ('Python','Java','Javascript')
# print(my_tuple)
# print(my_tuple[1])
# my_tuple[1]='C++'

# my_list = ['Kaushik','Prativ','Sherina','Rudransh']
# print(len(my_list))
# s = "Python"
# print(len(s))

# my_list = []
# my_list.append(456)
# my_list.append(123)
# my_list.append(789)
# print(my_list)

# my_list = [456,123,789]
# my_list.insert(1,'svr')
# print(my_list)

# my_list = [456,123,789]
# print(my_list)
# my_list.remove(123)
# print(my_list)
# my_list.pop()
# print(my_list)
# print(my_list)
# my_list.pop(1)
# print(my_list)

# my_list = ['a','b','c']
# print(my_list)
# my_list.clear()
# print(my_list)

# list_1 = ['a','b','c']
# list_2 = ['d','e','f']
# print(list_1)
# list_1.extend(list_2)
# print(list_1)

# list_3 = list_1 + list_2
# print(list_3)
# print(list_1)
# print(list_2)

# num_list = [12,45,23,39,97,84]
# print(num_list)
# num_list.sort()
# print(num_list)
# num_list.sort(reverse=True)
# print(num_list)

# name_list = ['Apple','Banana']
# fruits_list = name_list
# fruits_list.append('Cherry')
# print(fruits_list)
# print(name_list)

# new_fruits = fruits_list.copy()
# new_fruits.append('guava')
# print(new_fruits)
# print(fruits_list)

# places= ['TN','KL','AN','KA','TS']
# print(places)
# print(places.index('AN'))

# marks = [90,95,90,99,89]
# print(marks)
# print(marks.count(90))

# Dictionary
# multiple data points
# {}
# key,value pair
# key: value
# {key1:value1,key2:value2,...}
# key->immutable, unique, str, int, tuple
# value->any datatypes
# indexing -> key

# empty_dict = {}
# print(empty_dict)
#
# int_dict ={1:'Kaushik',2:'Prativ',3:'Sherina',4:'Rudransh'}
# print(int_dict)
#
# str_dict = {'name':'Ramprabu','class':'Python'}
# print(str_dict)

# Type Conversion
# Implicit - automatic type conversion
# a = 10 #int -> float 10->10.0
# b = 15.5 #float
# c = a + b
# print(c)
# Explicit
# int
# a = 10
# b = "15"
# c = a + b
# print(c)
# str with int
# add

# # Explicit type conversion or Type Casting
# a
# # "15" -> 15
# a=int(a)
# a=float(a)
# a=str(a)

# a = 10 #int
# b = "15"
# b = int(b)
# c = a + b
# print(c)

# a
# a = list(a)
# a = tuple(a)

# details = ('ram',30,'mdu')
# details = list(details)
# details[0] = "Ram"
# details = tuple(details)
# print(details)

# x
# float(x)

# a = input()

# print('Hellooo')
# print()
# print('hello','world','welcome')
# # default seperator = space
# print('hello','world','welcome',sep=" ")
# print('hello','world','welcome',sep="--->")
# print('hello',sep="--->")

# print('Hiii')
# print('Bye',end="\n")
# print('Bye',end="-----")
# print('hello','world','welcome',end=">>>>")
# print('hello','world','welcome',sep="--->",end="<<<")

# Operators
# + -> addition
# 3 + 9 -> + operator, 3,9 operands
# 7 types of operators
#
# Arithmetic Operators
# Comparison operators
# Logical operators
# Bitwise operators
# Identity operators
# Membership operators
# Assignment Operators


# Arithmetic Opertors
# + if operands are int then addition
# print(3+9)
# + if operands are str then concatenation
# print("Python"+"Programming")
# print(3+"abc")
# print('abc'+3)
# - subtraction
# print(5-3)
# * multiplication
# print(4*2)
# / division
# print(31/5)
# // floor division
# print(10/3)
# print('quotient',10//3)
# % modulo
# print('remainder',10%3)
# ** power or exponential
# print(5 ** 4)

# Comparison Operators
#
# print('> greater than')
# print('5 > 3',5>3)
# print('3 > 5',3>5)
#
# print('< less than')
# print('3 < 5',3<5)
# print('5 < 3',5<3)
#
# print('== value equals')
# print('3 == 3',3==3)
# print('3 == 5',3==5)
#
# print('!= value not equals')
# print('3 != 5',3!=5)
# print('3 != 3',3!=3)
#
# print('>= greater than or equals')
# print('5 >= 3',5>=3)
# print('5 >= 5',5>=5)
# print('3 >= 5',3>=5)
#
# print('<= lesser than or equals')
# print('3 <= 5',3<=5)
# print('5 <= 5',5<=5)
# print('5 <= 3',5<=3)

# Identity Operator
# is
# is not
# a = 10
# b = 15
# c = 15
# print('a is b',a is b)
# print('b is c',b is c)
# print('a is not b',a is not b)
# print('b is not c',b is not c)

# logical operators or boolean operators
# or -> addition
# print(True or True) #(1+1) True
# print(True or False) #True
# print(False or True) #True
# print(False or False) #False
# # and -> multiplication
# print(True and True) #(1*1) True
# print(True and False) #False
# print(False and True) #False
# print(False and False) #False
# # not
# print(not True)
# print(not False)

# Bitwise Operators
# print(5 & 3)
# 0101010110
# 1101011010
# 1001010101

# membership operator
# in
# not in
# a = 6
# b = 1
# c = [1,2,3,4,5]
# print(a in c)
# print(b in c)
#
# print(a not in c)
# print(b not in c)

# Assignment operator
# a = 10
# 7 augmented assignment operators or
# compound assignment

# a += 5 #a+5-> 10+5 -> 15 -> a = 15
# print(a)
# # -=
# # *=
# # /=
# a //= 4
# print(a)
# a %= 3
# print(a)
# a = 5
# a **= 2
# print(a)

# Python program to find the number of toys
# x has if he/she own
# 2 aeroplanes, 5 helicopters and 11 trains.

# aeroplanes = 2
# helicopters = 5
# trains = 11
# toys = aeroplanes + helicopters + trains
# print('Total no of toys is',toys)

# "Concatenation:
# Python program to generate full name
# given two variable first_name (has the first name stored in it)
# and last_name (has last name stored in it)"

# first_name = "Ramprabu"
# last_name = "S V"
# full_name = first_name + last_name
# print('My full name is',full_name)

# petrol = 14
# bikes = 4
# petrol_in_bike = petrol / bikes
# print('petrol in each bike is',petrol_in_bike,'litres')

# persons = 12
# cups = 5
# person_per_cup = persons // cups
# print('Number of persons per cup',person_per_cup)
# persons_left = persons % cups
# print(persons_left,'persons didnt get to ride')

# # logical operators or boolean operators
# # True -> 1
# # False -> 0
# # or -> addition
# print(True or True) #(1+1) True
# print(True or False) #True
# print(False or True) #True
# print(False or False) #False
# # and -> multiplication
# print(True and True) #(1*1) True
# print(True and False) #False
# print(False and True) #False
# print(False and False) #False
# # not
# print(not True) #False
# print(not False) #True

# ride in a theme park
# height and weight
# 100 cms or 40kgs
# (height>100 or weight >40)
# (height>100 and weight >40)

# Identity Operator
# is ==
# is not !=
# a = 10
# b = 15
# c = 15
# print('a is b',a is b)
# print('b is c',b is c)
# print('a is not b',a is not b)
# print('b is not c',b is not c)

# Bitwise Operators
# print(5 & 3)
# 0101010110
# 1101011010
# 1001010101

# membership operator
# in
# not in
# a = 6
# b = 1
# c = [1,2,3,4,5]
# print(a in c)
# print(b in c)
#
# print(a not in c)
# print(b not in c)

# age = int(input('Enter ur age: '))
# if (0<age<=5):
#     print('KG')
# elif (5<age<=10):
#     print('Primary')
# elif (10<age<=16):
#     print('Secondary')
# elif (16<age<=18):
#     print('Higher secondary')
# else:
#     print('Does not belong to school')

# user_day = input('Enter a day: ')
# if user_day == 'Monday':
#     print('First day of the week')
# elif user_day == 'Saturday':
#     print('Weekend')

# print('Lets play Rock Paper Scissors')
# p1 = input("Choose r or p or s: ")
# p2 = input("Choose r or p or s: ")
# r p s
# r p s
# 3^2=9
# r s
# s r
# p s
# s p
# r p
# p r
# rr ss pp dont do this
# if (p1 == 'r' and p2 == 's'):
#     print('p1 wins')
# elif (p1 == 's' and p2 == 'r'):
#     print('p2 wins')
# elif (p1 == 's' and p2 == 'p'):
#     print('p1 wins')
# elif (p1 == 'p' and p2 == 's'):
#     print('p2 wins')
# elif (p1 == 'p' and p2 == 'r'):
#     print('p1 wins')
# elif (p1 == 'r' and p2 == 'p'):
#     print('p2 wins')
# elif (p1 == p2):
#     print('It is a tie')
# else:
#     print('Invalid input')

# n = int(input('Enter no: '))
# if (n%2 == 0):
#     print('Even')
# else:
#     print('Odd')

# for iterating_variable in iterable:
#     statements with iterating_variable

# for -> keyword
# iterable -> list, tuple or string
# in -> operator
# iterating var -> temporary variable to store

# for i in ['kaushik','prativ','rudransh']:
#     print(i)

# for i in "Python":
#     print(i)

# range(10)
# [0,1,2,3,4,5,6,7,8,9]
# range(5)
# [0,1,2,3,4]
# range(4,10)
# [4,5,6,7,8,9]

# for i in range(10):
#     print(i)
#
# for i in range(4,10):
#     print(i)

# generate acronym
# Indian Space Research Organization
# ISRO

# user_input = input('Enter: ').split()
# acro = ""
# for each_word in user_input:
#     acro += each_word[0]
# print(acro)

# palindrome
# s = input('enter word: ')
# rev_s = ""
# for letter in s:
#     rev_s = letter + rev_s
# if s == rev_s :
#     print(s,'is a palindrome')
# else:
#     print(s,"is not a palindrome")

# Multiplication table generator
# num = int(input('Choose a no: '))
# # 1 x 3 = 3
# # 2 x 3 = 6
# for i in range(1,11):
#     print(i,'x',num,'=',i*num)

# n = int(input('Enter: '))
# ans = 0
# for i in str(n):
#     ans += int(i)
# print('sum of digits of',n,'is',ans)

# armstrong no
123 ->
1**3 -> 1
2**3 _> 8
3**3 -> 27
1+8+27 -> 36

153
1
125
27
153