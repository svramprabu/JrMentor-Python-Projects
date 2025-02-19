# s = "     python PROGRAMMING   "
# print(s)
# print(s.upper())
# print(s.lower())
# print(s.capitalize())
# print(s.title())
# print(s.swapcase())
# print(s.strip())
# print(s.split())
# from numpy.random import exponential
# from main_projects.hangman import user_input

# s = ""
# s = "a"
# s = "sjlhb28rb23r"

# s = 'HackerKid Python'
# print(s)
# print(s[3])
# print(s[8])
# print(s[9])
#
# print(s[-1])
# print(s[-5])

# string slicing
# s[start:stop] start-> including stop-> excluded
# s = "HackerKid"
# print(s)
# print(s[3:7]) #3,4,5,6
# print(s[3:])
# print(s[:7])
# print(s[:])
# s[start:stop:step=1]
# print(s[3:7:1])
# print(s[2:8:2])
# print(s[::2])
# print(s[::-1]) #reversing a string
# print(s[::-1]) #reversing a string

# s = "Hackerkid"

# s[0]='h'
# immutability
# immutability
# s = "hackerkid"

# s = "Hi ram, my name is ram and i am from some location"
# print(s.find('ram'))
# print(s.rfind('ram'))

# s = "Hi ram, my name is ram and i am from some location"
# print(s.replace('ram','Ramprabu'))
# print(s)

# List, Tuple and Dictionary

# List and Tuple
# Ordered values
# comma seperated values
# val1, val2, val3
# [] -> list ()-> tuple

# integer list
# int_list = [1,234,66,34,46]
# print(int_list)
# #integer tuple
# int_tuple = (1,234,66,34,46)
# print(int_tuple)

# string list
# str_list = ['Nikhil','Nickson','Aaron','Faizal']
# print(str_list)
# str_tuple = ('Nikhil','Nickson','Aaron','Faizal')
# print(str_tuple)

# empty_list = []
# print(empty_list)
# empty_tuple = ()
# print(empty_tuple)

# mixed_list = [123,2345.44356,'python']
# print(mixed_list)
# mixed_tuple = (123,2345.44356,'python')
# print(mixed_tuple)

# nested_list = ['1a',['a','b','c']]
# print(nested_list)
# nested_tuple = ('1a',('a','b','c'))
# print(nested_tuple)

# my_list = ['a','b','c']
# print(my_list)
# my_list[1]='Python'
# print(my_list)
#
# my_tuple = ('a','b','c')
# print(my_tuple)
# my_tuple[1]='Python'

# my_list = ['a','b','c']
# print(my_list)
# my_list.append('d')
# print(my_list)
#
# my_list.insert(2,'Z')
# print(my_list)
#
# my_list.remove('Z')
# print(my_list)
# my_list.remove('e')

# my_list.pop()
# print(my_list)
#
# my_list.pop(0)
# print(my_list)
#
# my_list.clear()
# print

# fruits = ['apple','banana','orange']
# veggies = ['beans','carrot','cabbage']
# fruits.extend(veggies)
# print(fruits)
# groceries=fruits+veggies
# print(groceries)
# print(fruits)
# print(veggies)

# my_list = [1,5,8,3,9]
# print(my_list)
# my_list.sort()
# print(my_list)
# my_list.sort(reverse=True)
# print(my_list)

# animals = ['cat','dog','horse']
# print(animals)
# domestic_animals = animals #ref copy of the original list
# domestic_animals[1]='wolf'
# print(animals)
# print(domestic_animals)
#
# wild_animals = animals.copy() #copy of the list
# wild_animals[0]='Lion'
# print(animals)
# print(wild_animals)

# group_names = ['Nickson','Nikhil','Faizal','Aaron']
# print(group_names.index('Faizal'))
# print(group_names.index('Ram'))

# group_names = ['Nickson','Nikhil','Faizal','Aaron','Aaron']
# print(group_names.count('Aaron'))
# print(group_names.count('Nikhil'))
# print(group_names.count('aaron'))

# group_names = ['Nickson','Nikhil','Faizal','Aaron','Aaron']
# print(len(group_names))
# s = "Python programming"
# print(len(s))

# fname,lname = ['Ramprabu','SV'] #unpacking a list
# print(fname)
# print(lname)


# Type conversion
# Implicit
# Explicit or Type Casting

# a = 123 #123.0
# b = 45.67
# addition = a+b
# print(addition)

# a = "123"
# b = 345
# c = a+b
# print(c)

# a = 123
# b = "345"
# c = a+b
# print(c)

# Explicit - Type Casting

# a
# int(a)
# float(a)
# str(a)

# a = 123
# b = "345"
# b = int(b)
# c = a+b
# print(c)

# a
# list(a)
# tuple(a)

# name = ('Python','Programming')
# name = list(name)
# name[0]='XXX'
# name = tuple(name)
# print(name)

# Dictionary
# {}
# Unordered list of values
# key, value pair
# key:value
# {key1:value1,key2:value2,...}
# key -> unique, immutable -> tuple, str, int
# value -> any datatype
# x[key] -> accessing an element in a dict

# empty_dict = {}
# print(empty_dict)
#
# int_dict = {1:'Eng',2:'Math',3:'EVS'}
# print(int_dict)
#
# str_dict = {'fname':'Ramprabu','lname':'SV'}
# print(str_dict)
#
# mixed_dict = {1:'Python','class':'HackerKid'}
# print(mixed_dict)
#
# print(mixed_dict[1])
# print(mixed_dict['class'])

# input()

# print() #empty line
# print("hello",'world')
# print("hi","all",sep=" ")
# print("hi","all")
# print("hi","all","welcome",sep="===")

# Nikhil--->Ronit

# print('Hiiii')
# print('Hiiii',end="\n")
# print('Helloo',end="-----")
# print('Helloo')

# Operators - symbols
# + -> addition
# 3 + 9
# 3,9 operands
# + operator

# Arithmetic Opertors
# + if operands are int then addition
# print(3+9)
# + if operands are str then concatenation
# print("Nikhil"+"Ronit")
# print(3+"abc")
# print('abc'+3)
# - subtraction
# * multiplication
# / division
# print(3/1)
# // floor division
# print(10/3)
# print('quotient',10//3)
# % modulo
# print('remainder',10%3)
# ** power or exponential
# print(5 ** 4)

# Comparison Operators

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

# flow control
# 1. conditional statements
# 2. loops
# 3. functions

# conditional statements
# 1. if
# syntax
# if (condition):
#      #4 individual spaces or 1 tab space
#     statement1
#     statement2
#     statement3
# some other statement
# if (10>5):
#     print("ten ")
#     print("is greater than ")
#     print("five")
# n = int(input('Enter a no: '))
# if (n>0):
#     print("positive no entered")
# 2. else
# if(condition):
#     statement
# else:
#     alternative statement
# age = int(input('age='))
# if (age > 18):
#     print('Eligible to vote')
# else:
#     print('Not eligible to vote')

# name = input('Enter name: ')
# if ('a'in name or 'e' in name or 'i' in name or 'o' in name or 'u' in name):
#     print('nice')
# else:
#     print('not nice')

# 3. elif
# if (condition1):
#     statement1
# elif (condition2):
#     statement2
# .
# .
# else:
#     alternative statement

# day of the week
# sunday - fun day
# saturday - weekend
# friday - end of a long week
# mon,tue,wed,thu - yet another day

# age -
# kg 0-5
# primary 6-10
# secondary 11-16
# high school 16-18
# do not belong 18 and above
# age = 30
# if (0<age<5):
#     print("kg")

# rock paper scissor
# p1 r,p,s
# p1 = input('Choose rock(r) or paper(p) or scissors(s):').lower()[0]
# p2 r,p,s
# p2 = input('Choose rock(r) or paper(p) or scissors(s):').lower()[0]

# print(p1,p2)
# if (p1 == p2): #r r s s p p
#     print('Draw')
# elif (p1 == 'r' and p2 == 's'):
#     print('player 1 wins')
#
# else:
#     print('Invalid input')

# 3^2 - 9 combinations
# r p
# p r
# r s
# s r
# p s
# s p
# r r
# s s
# p p

# r or R or rock or Rock string methods, string access

# age=int(input("enter your age"))
# if(0<age<5):
#     print("kindergarden")
# if(5<age<=10):
#     print("primary")
# if(10<age<=16):
#     print("secondary")
# if(16<age<=18):
#     print("highschool")
#
# age=int(input("enter your age"))
# if(0<age<5):
#     print("kindergarden")
# elif(5<age<=10):
#     print("primary")
# elif(10<age<=16):
#     print("secondary")
# elif(16<age<=18):
#     print("highschool")
# else:
#     print("completed schooling")

# loops
# for and while loop
# finite cycles - for loop
# depends on the condition - while

# for iterating_variable in iterable:
    # statement iterating_variable
# list,tuple,string
# iterating_variable - temporary var

# for i in [1,2,3,4,5]:
#     print(i)

# for i in "Python":
#     print(i.upper())

# for i in range(10): #[0,1,2,3,...9]
#     print('python')
#
# for i in range(11):
#     print(i)

# for i in range(5,10,2):
#     print(i)

# input from user for a string
#     no of vowels in the string

# s = input('Enter a word: ')
# v = "aeiou"
# n = 0
# for i in s:
#     if i.lower() in v:
#         n += 1
# print(n,'vowels in',s)

# Python program that accepts a string
# calculates the number of digits and letters.

# s = input('Enter: ')
# d = 0
# a = 0
#
# for i in s:
#     if i.isalpha():
#         a += 1
#     elif i.isdigit():
#         d += 1
# print(a,"no of alphabets in",s)
# print(d,"no of digits in ",s)

# n = int(input('Enter a no:'))
# d = 0
# s = 0
# for i in str(n): #n should be iterable str, list, tuple
#     # print(i)
#     d+=1
#     s+=int(i) #s int + i str
# print(d,"is the no of digits in",n)
# print(s,'is the sum of digits in',n)

# 153
# 1**3 - 1
# 5**3 - 125
# 3**3 - 27
# 1+125+27= 153

# n = int(input('Enter a no:'))
# s = 0
# for i in str(n): #n should be iterable str, list, tuple
#     s+=int(i)**3
# if s == n:
#     print('Armstrong no')
# else:
#     print('not an armstrong no')

# apple
# a
# pple - string slicing
# print if exits in remaining string

# user_input=input("Enter here : ").split()
# acro = ""
# for each_word in user_input:
#     acro += each_word[0]
# print(acro.upper())

# saved_pwd = "pass123"
# for tries in range(3):
#     user_pwd = input('Enter pwd: ')
#     if user_pwd != saved_pwd:
#         print('Wrong pwd, Try again')
#     else:
#         break
# print('Success')

# for i in range(10):
#     if i == 4:
#         continue
#     print(i)

# pwd program

# wrong password increace attempts by 1
# if pass is semi correct attempts should remain same
#     "pass" in user_pwd

# saved_pwd = "pass123"
# attempts = 0
# for tries in range(10):
#     user_pwd = input('Enter pwd: ')
#
#     if user_pwd != saved_pwd:
#         if "pass" in user_pwd:
#             print('semi correct',
#                   attempts,'attempt(s) made')
#             continue
#         attempts += 1
#         print('Wrong pwd, Try again',
#               attempts,'attempt(s) made')
#     else:
#         print('Success')
#         break

# while (condition):
#     statement

# while (5>3):
#     print('5>3')

# i = 0
# while (i<10):
#     i += 1
#     print(i)

# num = int(input('Enter no: '))
# n = num
# res = 0
# while(n > 0):
#     last_digit = n % 10 #123 -> 123 % 10 = 3
#     n //= 10 #123 / 10 -> 12.3 // -> 12
#     res += last_digit**3
# if (res == num):
#     print('Armstrong')
# else:
#     print('not armstrong')

# saved_pwd = "pass123"
# user_pwd = ""
# attempts = 0
# while(saved_pwd != user_pwd):
#     print(3-attempts,'attempts left')
#     user_pwd = input('Enter pwd: ')
#     if user_pwd != saved_pwd:
#         if ("pass" in user_pwd or "123" in user_pwd):
#             print('semi correct',
#                   attempts,'attempt(s) made')
#             continue
#         attempts += 1
#         if (attempts == 3):
#             print(attempts,'attempts made')
#             print('you have exhausted the no of attempts')
#             break
#         print('Wrong pwd, Try again',
#               attempts,'attempt(s) made')
#     else:
#         print('Success')
#         break


# print('abc') #arguments
# int()
# float()
# car()

# user-defined
# def car(paramaters): #parameters -> variables
#     statements
#     print(paramaters) #eg statement
#     return 'xyz'

# print()

# type 1 fn no parameters no return

# def func1():
#     fname = input('First name: ')
#     lname = input('Last name: ')
#     print(fname,lname)
#
# func1()

# type 2 fn no parameters but return a value

# def func2():
#     num_1 = int(input('a='))
#     num_2 = int(input('b='))
#     return num_1+num_2
#
# print(func2()) #method 1
# ans = func2() #method 2
#
# if (func2()>18): #method 3
#     print('Valid to vote')
# else:
#     print('not eligible')
# print(input())

# type 3 fn no return but gets parameters or arguments

# def func3(name):
#     print(name)

# func3('Python') #passing the data to the function
# pass by value
# name = 'python'
# n = 'Python'
# func3(n)
#pass by reference
# name = n
# name = 'Python'
# func3(name)

# type 4 both arguments and return

# def func4(age):
#     if (age>18):
#         return "Can Vote"
#     else:
#         return "Cannot Vote"
#
# age = int(input('Enter ur age: '))
# print(func4(age))

# calculator.py