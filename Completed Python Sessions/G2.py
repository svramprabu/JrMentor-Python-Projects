# var_123 = 12345
# print(var_123)

# a = 123
# print(a)
# print(type(a))
#
# b = 123.45
# print(b)
# print(type(b))
#
# c = 'ABCDabcd1234!@#$'
# print(c)
# print(type(c))

# s = 'Completed Python Sessions'
# print(s)
# print(s[0])
# print(s[2])
#
# print(s[-1])
# print(s[-2])

# ab = 'abcdefghijklmnopqrstuvwxyz' #creating a string of alphabets
# a e i o u

# print(ab[0])
# print(ab[4])
# print(ab[8])

# example_list = [1,2,3,4,5] #integer list
# print(example_list)
# ex_list = ['jaswanth','aatreyee','samyuktha','surya','mukundan'] #strign only list
# print(ex_list)
# my_list = [123,456,67.89,'Completed Python Sessions'] #mixed list
# print(my_list)
# empty_list = []
# print(empty_list)
# # Nested list
# nested_list = [123,[1,2,3]]
# print(nested_list)

# example_tuple = (1,2,3,4,5) #integer tuple
# print(example_tuple)
# ex_tuple = ('jaswanth','aatreyee','samyuktha','surya','mukundan')
# print(ex_tuple)
# my_tuple = (123,456,67.89,'Completed Python Sessions') #mixed tuple
# print(my_tuple)
# empty_tuple = ()
# print(empty_tuple)
# nested_tuple = (123,(1,2,3))
# print(nested_tuple)

# Accessing elements in List and Tuple
# example_list = ['jaswanth','aatreyee','samyuktha','surya','mukundan']
# print(example_list)
# print(example_list[1])
#
# example_tuple = ('jaswanth','aatreyee','samyuktha','surya','mukundan')
# print(example_tuple)
# print(example_tuple[1])

# Mutability
# Replace a particular value alone
# List is Mutable
# example_list[4]='Completed Python Sessions'
# print(example_list)
# Tuple is Immutable
# example_tuple[4]='Completed Python Sessions'
# example_tuple = ('jaswanth','aatreyee','samyuktha','surya','Completed Python Sessions')
# print(example_tuple)

# Dictionary
# empty_dict = {} #empty dictionary
# print(empty_dict)
# ex_dict = {1:'Apple',2:'Ball'} #dict with int keys
# print(ex_dict)
# my_dict = {'name':'Completed Python Sessions','age':45} #dict with string keys
# print(my_dict)
# my_dict = {1:'Hackerkid','Class no':5} #mixed dict
# print(my_dict)

# Accessing elements in a dictionary
# my_dict = {1:'Hackerkid','Class no':5} #mixed dict
# print(my_dict)
# print(my_dict[1])
# print(my_dict['Class no'])

# a = 10
# b = 15.5
# add = a + b
# print(add)

# a
# a = int(a)
# b = float(a)
# a = str(a)



# a = 10
# b = '15'
# b = int(b)
# add = a + b
# print(add)

# name = input('Enter your name ')
# print(name)
# print(type(name))
#
# age = int(input('What is ur Age: '))
# print(age)
# print(type(age))
#
# weight = float(input('What is ur weight'))
# print(weight)
# print(type(weight))

# a = 10
# b = 11
# c = 12
# print(a)
# print(b)
# print(c)
# print(a,b,c)
# print(a,b,c,sep=' ')
# print(a,b,c,sep='')
# print(a,b,c,sep='->')
#
# print('abcdefg')
# print('abcdefg',end='\n')
# print('abcdefg',end='--->')
# print('ijklmnop')
# print(a,b,c,sep='->',end='$$$')

# a = 10
# b = 15
# print(a,b)
# print('The variables are',a,'and',b) #type 1
# print(f"The variables are {a} and {b}") #type 2

# Making a self introduction using f string
# n = input('Enter your name: ')
# c = input('Enter your class: ')
# s = input('Enter your school: ')
# h = input('Enter your hobby: ')
# l = input('Enter your location: ')
# print(f"Hi My name is {n} and I am studying in class {c} in {s} school "
#       f"My favourite hobby is {h} and I live in {l}")

# Operators

# x = 11
# y = 2
# print('x+y=',x + y) #addition
# p = '10'
# q = '15'
# print('p+q=',p+q) #concatenation
# a = 'Completed Python Sessions'
# b = 'Programming'
# print('a+b=',a + b) #concatenation
#
# print('x-y=',x - y) #subtraction
# print('x*y=',x * y) #multiplication

# / % //
# x = 11
# y = 3
# print('x / y =',x/y) #Division
# print('x // y =',x//y) #Floor Division
# print('x % y =',x%y) #Modulus
#
# #Exponentiation
# print('x**y=',x**y) #11 * 11 * 11

# print('> greater than')
# print('5 > 3 =',5>3)
# print('3 > 5 =',3>5)
#
# print('< less than')
# print('3 < 5 =',3<5)
# print('5 < 3 =',5<3)
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
#
#


# "Concatenation:
# Completed Python Sessions program to generate full name given two variable
# first_name (has the first name stored in it) and
# last_name (has last name stored in it)"
# first_name = input('Enter your firstname: ')
# last_name = input('Enter your last name: ')
# full_name = first_name + last_name
# print(f'My full name is {full_name}')

# Completed Python Sessions program to find the number of toys x has
# if he/she own 2 aeroplanes, 5 helicopters and 11 trains.

# aeroplanes = 2
# helicopters = 5
# trains = 11
# number_of_toys = aeroplanes + helicopters + trains
# print(f"The total number of toys x has is {number_of_toys}")

# Completed Python Sessions program to find the cost of apples
# if x plans to buy 8 apples at the price of 17 each

# apples = 8
# price = 17
# cost_of_apples = apples * price
# print(f"Total cost of {apples} apples priced at {price} each is {cost_of_apples}")

# Completed Python Sessions program to find how many litres of petrol
# can be filled in 4 bikes given we have only 14 litres of petrol.

# bikes = 4
# petrol = 14
# petrol_in_bike = petrol / bikes
# print(f"each bike will have {petrol_in_bike}")

# Completed Python Sessions program to calculate the area of a square given the length of one side.
# length_of_side = 10
# area_of_the_square = length_of_side ** 2
# print(f" if the length is {length_of_side} then the area is {area_of_the_square}")

# height = int(input('Enter your height: '))
# if (height > 150):
#     print('Enjoy the ride')

# Get an input asking for the age
#     reply with 'you are eligible to vote' if he is more than 18 years
#     or 'you are not eligible' if he's not

# age = int(input('Enter your age: '))
# if (age > 18):
#     print('you are eligible to vote')
# else:
#     print('you are Not eligible')

# if condition:
# 	statement
# elif condition:
#   statement
# elif condition:
# 	statement
# .
# .
# .
# else:
# 	statement

# if
#
# if else
#
# if elif
#
# if elif else

# a = int(input('Enter a num: '))
# if (a > 5):
#     print('Something')
# elif (a < 5):
#     print('Nothing')

# day_of_week = input('Enter the day of week: ').lower()
# if (day_of_week == 'monday'):
#     print('First day of the week')
# elif (day_of_week == 'friday'):
#     print('Fun day')
# elif (day_of_week == 'sunday' or day_of_week == ' saturday'):
#     print('Jolly day')
# else:
#     print('Just yet another day of the week')

# age = int(input('Enter ur age: '))
# if (age < 5):
#     print('KG')
# elif (age < 10):
#     print('Primary')
# elif (age < 15):
#     print('Secondary')
# elif (age < 18):
#     print('Higher Secondary')
# else:
#     print("Does not belong to school")
# kg is below 5
# primary is below 10
# secondary is below 15
# higher secondary is below 18
# does not belong in school

# num = int(input('enter the num: '))
# if (num % 2 == 0):
#     print(f'{num} is an even number')
# else:
#     print(f'{num} is an odd number')

# for loop
# loops.py
# Syntax:
# for iterating_variable in sequence:
#     Statement(s)
# []
# my_list = ['Boomika','Dakshesha','Eniyavan']
# for i in my_list:
#     print(i)
# # 'dlsjfb'
# my_string = 'Completed Python Sessions programming'
# for i in my_string:
#     print(i)
# # n
# # 10
#
# for i in range(15): #[0,1,2...9]
#     print(i)
#
# for i in range(3):
#     print(my_list[i])

# Declare a list of fruits and vegatable (6 items)
# print the items one by one

# United States
# US
# user_input = input('Enter: ').split()
# print(user_input)
# result = ''
# for word in user_input:
#     result += word[0]
# print(result)

# s = input('Enter the word: ')
# vowels = 'AEIOUaeiou'
# answer = 0
# for each_char in s:
#     if (each_char in vowels):
#         answer += 1
# print(f"Number of vowels in {s} is {answer}")

# user_input = input('Paste the content here: ').split()
# no_of_words = 0
# for each_word in user_input:
#     no_of_words += 1
# print(f'Number of words in the paragraph is {no_of_words}')

# Completed Python Sessions program to count the number of digits in a number
# and find the sum of them

# Method 1
# number = int(input('Enter a number: '))
# str_num = str(number)
# no_of_digits = len(str_num)
# print(f'Number of digits in {number} is {no_of_digits}')
#
# sum_of_num = 0
# for each in str_num:
#     sum_of_num += int(each)
# print(f'Sum of digits of {number} is {sum_of_num}')

# Multiplication table
# table_no = int(input('Enter the table no: '))
# for i in range(1,11):
#     print(f"{i} X {table_no} = {i*table_no}")

# * * *
# * * *
# * * *

# for row in range(5):
#     for col in range(5):
#         print(f'{row}{col} ',end='')
#         # print(f'* ', end='')
#     print()

# *
# * *
# * * *
# * * * *
# * * * * *

# for row in range(5):
#     for col in range(row+1): # 1 2 3 4 5
#         print('* ', end='')
#     print()

# * * * * *
# * * * *
# * * *
# * *
# *

# for row in range(5):
#     for col in range(5-row): # 5 4 3 2 1
#         print('* ', end='')
#     print()


# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# for row in range(5):
#     for col in range(row+1): # 1 2 3 4 5
#         print(row+1, end='')
#     print()

# s = input('Enter the string: ')
# for n in range(2):
#     x = input(f'Enter letter {n} to search: ')
#     ans = 0
#     for i in s:
#         if (i == x):
#             ans += 1
#     print(f'There are {ans} {x} in {s}')

# while (condition):
#     statement

# i = 5
# while (i < 15):
#     print(i)
#     i += 1

# start = 10
# end = 25
#
# print("Using for loop")
# for i in range(start,end):
#     print(i)
#
# print("Using While loop")
# i = start
# while i < end:
#     print(i)
#     i += 1

# saved_password = 'pass123'
# user_password = ''
# while(user_password != saved_password):
#     user_password = input('Enter password: ')
#     if (user_password == saved_password):
#         print('Success')
#     else:
#         print("Try again")
# print('You entered the right password')

# import random
# chosen_no = random.randint(1,100)
# user_no = 0
# print('The range is between 1 and 100')
# while(user_no != chosen_no):
#     user_no = int(input('Enter no: '))
#     if (user_no > chosen_no):
#         print('choose a smaller no')
#     elif (user_no < chosen_no):
#         print('choose a bigger no')
#     else:
#         print(f"you found the number as {user_no}")
# print('Thank you for playing')

# num = int(input('Enter number: '))
# n = num
# digits=0
# sum_digits=0
# while (n>0):
#     print(n//10) #floor division
#     print(n%10) #modulo
#     sum_digits += n%10
#     digits += 1
#     n = n//10
# print(f'Number of digits in {num} is {digits}')
# print(f"sum of digits in {num} is {sum_digits}")

# 151
# 1 -> 1**3 -> 1
# 5 -> 5**3 -> 125
# 1 -> 1**3 -> 1
# 1+125+1=127
# not an armstrong
#
# 153
# 1 -> 1
# 5 -> 125
# 3 -> 27
#
# 1+125+27 = 153


# Break

# i = 0
# while (i < 10):
#     print(i)
#     if (i == 4):
#         break
#     i+=1

# saved_password = 'pass123'
# while(True):
#     user_password = input('Enter password: ')
#     if (user_password == saved_password):
#         print('Success')
#         break
#     else:
#         print("Try again")
# print('You entered the right password')

# continue

# i = 0
# while(i<10):
#     i+= 1
#     if (i == 6):
#         continue
#     print(i)

# saved_password = 'pass123'
# while(True):
#     user_password = input('Enter password: ')
#     if (user_password == saved_password):
#         print('Success')
#         break
#     else:
#         if ('pass' in user_password):
#             print('Semi correct')
#             continue
#         print("Try again")
# print('You entered the right password')

# task-manger.py

# list_of_tasks =[]
#
# print("Welcome to my Task manager Application")
# while(True):
#     user_option = int(input('\n1.Add a task'
#                             '\n2.Remove a task'
#                             '\n3.Search for a task'
#                             '\n4.Print all tasks'
#                             '\n5.Number of tasks'
#                             '\n0.Exit'
#                             '\nEnter Option: '))
#     if user_option == 1:
#         print('Lets add a task')
#         task = input('Enter task name: ')
#         if task not in list_of_tasks:
#             list_of_tasks.append(task)
#             print('Task added successfully')
#         else:
#             print('Task already in list')
#     elif user_option == 2:
#         print('Lets remove a task')
#         task = input('Enter task name: ')
#         if task in list_of_tasks:
#             list_of_tasks.remove(task)
#             print('Task removed successfully')
#         else:
#             print('Task not found in list')
#     elif user_option == 3:
#         print('Lets search for a task')
#         task = input('Enter task name: ')
#         if task in list_of_tasks:
#             print("Task found")
#         else:
#             print("Task not found")
#     elif user_option == 4:
#         print('\nAvailable tasks are')
#         for each_task in list_of_tasks:
#             print(f"-> {each_task}")
#     elif user_option == 5:
#         print(f"Number of tasks available are {len(list_of_tasks)}")
#     elif user_option == 0:
#         print('Thank you for using my application')
#         break
#     else:
#         print("Invalid Option")

# Type 1 no argument and no return
# def addition():
#     a = 10
#     b = 20
#     add = a+b
#     print(f'Addition of {a} and {b} is {add}')

# addition()
# print(addition())
# x = input('Name?')
# print(x)

# print(input('age?'))

# Type 2 no argument but return a value
# def func2():
#     b = 45
#     return b

# print(func2())

# Type 3 no return but has argument

# def func3(num):
#     print(f"Number is {num}")

# func3(50) #pass by value
# s = 50
# func3(s) #pass by reference

# Tyoe 4
# def func4(name):
#     return f"Owner name is {name.upper()}"
#
# print(func4('ramprabu'))

# functions.py
# def oddeven():
#     n = int(input('Enter num: '))
#     if (n % 2 == 0):
#         print(f'{n} is Even')
#     else:
#         print(f'{n} is Odd')
# oddeven()

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
#     return (f"Subtraction of {a} and {b} is {sub}")
# def mul(a,b): #type 3
#     mul = a * b
#     print(f"Multiplication of {a} and {b} is {mul}")

# def div(a,b): #type 4
#     div = a / b
#     return(f"Division of {a} and {b} is {div}")
#
# print("Welcome to my calculator program")
# while True:
#     user_option = int(input('\n1.Addition\n2.Subtraction'
#                             '\n3.Multiplication\n4.Division'
#                             '\nOption:'))
#     if (user_option == 1):
#         print('You chose Addition')
#         add()
#     elif user_option == 2:
#         print('You chose Subtraction')
#         print(sub())
#     elif user_option == 3:
#         print("You chose Multiplication")
#         mul()
#     elif user_option == 4:
#         print('You chose Division')
#         print(div())
#     else:
#         print('Thank you, Bye')
#         break

# from new_package import module1
# module1.func()

# import random
# random_number = random.randint(1,10)
# print(f'Random number is {random_number}')

# number_guessing_game.py
# import random
# chosen_number = random.randint(1,100)
# user_number = int(input('Guess the number: '))
# while True:
#     if user_number > chosen_number:
#         user_number = int(input('Choose a smaller no: '))
#     elif user_number < chosen_number:
#         user_number = int(input('Choose a bigger no: '))
#     else:
#         print('You found the number')
#         break

# file_operations.py
# open
# file = open('filename.extention','processing mode')
# Processing mode
# 4+2
# r - read (default) - throw error if file does not exist
# f = open('dakbooeni.txt')
# w - write - create if not present / truncate
# f = open('dakbooeni.txt','w')
# x - exclusive creation - create if not present / error
# f = open('dakbooeni.txt','x')
# a - append - create if not present / not truncate
# f = open('dakbooeni.txt','a')
# t - text mode(default)
# b - binary mode
# f = open('dakbooeni.txt','x+b')

# close
# f = open('dakbooeni.txt')
# f.close()
# read
# f = open('dakbooeni.txt')
# print(f.read())
# f.close()
# write
# f = open('dakbooeni.txt','w')
# f.write("We are practicing python")
# f.close()
# f = open('dakbooeni.txt')
# print(f.read())
# f.close()

# f = open('dakbooeni.txt','x')
# f.write("We are practicing python")
# f.close()
# f = open('dakbooeni.txt')
# print(f.read())
# f.close()

# f = open('dakbooeni.txt','a')
# f.write(" Successfully")
# f.close()
# f = open('dakbooeni.txt')
# print(f.read())
# f.close()

# RegularExpression
import re
# s = "Hello ball welcome all to my class"
# res = re.findall('all',s)
# print(res)

# res = re.search('all',s)
# print(res.start())
# print(res.end())

# res = re.split('all',s)
# print(res)

# res = re.sub(' ','--->',s)
# print(res)

# a = 10 #instance of class int
# print(type(a))

# oops.py
# class House:
#     owner = 'svr'
#     print(owner)
# my_house = House()
# class House:
#     def owner(self):
#         print('you')
#
# my_house = House()
# my_house.owner()

# class House:
#     def owner(self,o):
#         self.owner = o
#         print(self.owner)
#
# my_house1 = House()
# my_house2 = House()
# my_house1.owner('Daksheshaa')
# my_house2.owner('Boomika')

# class House:
#     def __init__(self,o): #constructor
#         self.owner = o
#         print(self.owner)
#
# my_house = House('Daksheshaa')


