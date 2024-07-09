# # print('Hi Soham More, Welcome to HackerKid')
# # variable_name = data
# # name = 123124 #declaring
# # print(name) #print
#
# #String Data type
# # name = 'soham82376$!$#'
# # print(name)
# # print(type(name))
#
# # String Access
# example_string = 'Hello World'
# print(example_string)
# # print(variable_name[index])
# print(example_string[4])
# print(example_string[6])
#
# # Declare a variable and
# # store a string of all english alphabets
# # print the vowels using string access
#
# # step 1 to declare a var with alphabets
#
# a = 1211414 #int
# b = 34.54646 #float
# c = 'lsdhjf2396dhjksbf4' #string
# d = True #Bool
#
# # example_list = [1,2,3,4,5]
#
#
# # empty_list
# empty_list=[]
#
# my_list = [1,2,3,4,5]
#
# my_list = [1,2,'hello','world',5.6,9.32]
#
# print(my_list)
# print(my_list[2]) #accessing a list element
#
# my_list = ['soham','more','python','hackerkid']
# print(my_list)
# my_list[2] = 'New data'
# print(my_list)
#


# Student Feedback generator
# name = 'Soham more'
# grade = 5
# talent = 'Aeroplane engineering'
# ambition = 'Game developer'
# place = 'India'
# print(f"Student named {name} in grade {grade} is very much talented in {talent} "
#       f"who is aiming to become {ambition} and he's from {place}")


# Length of the list
# len(name of the list)
# example
# list_of_numbers = [1,2,3,4,5,6,7]
# print(list_of_numbers)
# print(len(list_of_numbers)) #print the length of the list

# Words counter
# paragraph = input("paste the paragraph here: ") #"""Hi I'm Soham more"""
# words = paragraph.split()
# number_of_words = len(words)
# print(f'there are {number_of_words} words in the given paragraph')

# a = 5 #int
# b = 5.7 #float
# c = 'abc' #string

#input function
#Syntax: input(prompt)
# example
# x = input('Enter the data: ')
# print(x) #user typed data will be printed

# Student Feedback generator
# name = input('Enter your name: ')
# grade = input('Enter your grade')
# talent = input('What is your talent')
# ambition = input('Your ambition: ')
# place = input('Your country: ')
# print(f"Student named {name} in grade {grade} is very much talented in {talent} "
#       f"who is aiming to become {ambition} and he's from {place}")

# example
# print(name,grade,talent,sep='*') ctrl+/
# print(name,end='*')
# print(name,grade,sep='***',end='$$$')

# x = 5 #int
# y = 10.5 #float
# add = x + y #float + float
# print(add)

# Typecasting
# a
# int(a)
# float(a)
# str(a)

# x = 5
# y = '10'
# add = x + y
# print(add) #returns typeerror
#
# x = 5
# y = '10'
# y = int(y) #'10' -> 10
# add = x + y
# print(add) #returns 15

# How to add a data to a list or remove a data from a list
# list_of_items = []
#
# item1 = input('item1: ')
# item2 = input('item2: ')
# item3 = input('item3: ')
#
# print(list_of_items)
#
# # Add items to the list
# list_of_items.append(item1)
# list_of_items.append(item2)
# list_of_items.append(item3)
#
# print(list_of_items)
#
# #removing an items from list
# list_of_items.remove(item1)
# print(list_of_items)

# Comparison Operators

# 2 inputs
# input data - anything - int, float, string

# 1 output
# always True / False

# > Greater than
# eg: x>y
# if x is greater than y -> True
# if x is smaller than y -> False
# print('5>2',5>2) #True
# print('5>10',5>10) #False

# < Lesser than
# eg: x<y
# if x is less than y -> True
# if x is bigger than y -> False
# print('5<10',5<10) #True
# print('5<2',5<2) #False

# Python program to check password using while loop
# saved_password = 'soham123'
# user_password = ''
# while ( saved_password != user_password):
#     user_password = input('Enter password: ')
#     if (user_password == saved_password):
#         print('Success')
#     else:
#         print('Try again')
# print('You have been logged in successfully')

# Rock paper scissors:

# while(True):
#     p1 =
#     p2 =
#
#     if
#         ..

# i = 1
# while(i<10):
#     if (i == 7):
#         break
#     print(i)
#     i += 1

# saved_password = 'soham123'
# while(True):
#     user_password = input('Enter password: ')
#     if (user_password == saved_password):
#         print('Success')
#         break
#     else:
#         print('Try again')

# saved_password = 'soham123'
# count = 0
# while(True):
#     user_password = input('Enter password: ')
#     if (user_password == saved_password):
#         print('Success')
#         break
#     else:
#         count += 1
#         print(f'{count} wrong attempts made')
#         if (count == 3):
#             print('Sorry your attempts are over')
#             break
#         print('Try again')
#         print()

# i = 0
# while(i<10):
#     i += 1
#     if (i == 5):
#         continue
#     print(i)

# saved_password = 'soham123'
# count = 0
# while(True):
#     user_password = input('Enter password: ')
#     if (user_password == saved_password):
#         print('Success')
#         break
#     else:
#         if ('soham' in user_password):
#             print('Your password is semi correct')
#             continue
#         count += 1
#         print(f'{count} wrong attempts made')
#         if (count == 3):
#             print('Sorry your attempts are over')
#             break
#         print('Try again')
#         print()

# Type 1 function with no argument and no return
# def func1():
#     print('Hi from type 1 function')
#
# func1()

# Type 2 function with no argument but returns a value
# def func2():
#     return "Hello"
#
# print(func2())

# Type 3 function with no return value but argument
# def func3(var):
#     print(var)

# func3(123) #pass by value

# argument
# pass by value
# pass by ref

# a = 5
# func3(a) #pass by ref

# def add(): #type 1 no argument no return
#     a=int(input('a='))
#     b=int(input('b='))
#     addition = a+b
#     print(f"{a}+{b}={addition}")
#
# def sub(): #type 2 no arguments but return
#     a = int(input('a='))
#     b = int(input('b='))
#     subtraction = a-b
#     return f"{a}-{b}={subtraction}"
#
# def mul(a,b): #type 3 no return but argument
#     multiplication = a*b
#     print(f"{a}*{b}={multiplication}")
#
# def div(a,b): #type 4 with arguments and return
#     division = a / b
#     return f"{a}/{b}={division}"
#
# print('Welcome to my Calculator app')
# while(True):
#     user_option = int(input('Enter \n1.add \n2.sub \n3.mul \n4.div \n5.exit\nyour choice: '))
#     print()
#     if (user_option == 1):
#         print('You chose Addition feature')
#         add()
#     elif (user_option == 2):
#         print('You chose Subtraction feature')
#         print(sub())
#     elif (user_option == 3):
#         print('You chose Multiplication feature')
#         a = int(input('a='))
#         b = int(input('b='))
#         mul(a,b)
#     elif (user_option == 4):
#         print('You chose Division feature')
#         a = int(input('a='))
#         b = int(input('b='))
#         print(div(a,b))
#     elif (user_option == 5):
#         print('Thank you for using my app')
#         break
#     else:
#         print('Invalid choice please choose again')
#     print()

# from soham_package import module1
# module1.func()

# Dice simulator
# import random
# print('Welcome to my Dice Simulator')
# while(True):
#     user_choice = int(input('1. Roll 2.Exit'))
#     if (user_choice == 1):
#         dice_output = random.randint(1,6)
#         print(f'After rolling the dice you got a {dice_output}')
#     else:
#         print('thank you for rolling')
#         break

# import random
# start_range = int(input('Enter the starting range: ')) #1
# end_range = int(input('Enter the ending range: ')) #100
#
# chosen_number = random.randint(start_range,end_range) #43
#
# while(True):
#     user_number = int(input("Enter the number: ")) #21 53 50 45 40 41 43
#     if (user_number > chosen_number):
#         print('Enter a smaller number')
#     elif (user_number < chosen_number):
#         print('Enter a bigger number')
#     else:
#         print(f"You found the number {user_number}")
#         break

# def add_task(t):
#     if t not in tasks:
#         tasks.append(t)
#         return "Task added successfully\n"
#     else:
#         return "Task already present\n"
#
# def del_task(t):
#     if t in tasks:
#         tasks.remove(t)
#         return "Task Removed successfully\n"
#     else:
#         return "Task not present\n"
#
# def view_tasks():
#     print('\nTasks in your schedule are:')
#     for each_task in tasks:
#         print(f"- {each_task}")
#     print()
#
# def total_tasks():
#     return f'Total number of tasks available: {len(tasks)}\n'
#
# def search_task(t):
#     if t in tasks:
#         return True
#     return False
#
# tasks = []
# print("Welcome to my Task Manager Application")
#
# while(True):
#     user_option = int(input('1.Add a task\n2.Delete a task\n3.View all tasks\n4.Number of tasks\n5.Search\nYour choice here: '))
#     if (user_option == 1):
#         task = input('Enter the task: ')
#         print(add_task(task))
#     elif (user_option == 2):
#         task = input('Enter the task to be deleted: ')
#         print(del_task(task))
#     elif (user_option == 3):
#         view_tasks()
#     elif (user_option == 4):
#         print(total_tasks())
#     elif (user_option == 5):
#         task = input('Enter the task to search: ')
#         print(search_task(task))


# File operations
# Read Write Open Close

# open(file name, processing mode)
# f = open('soham.txt','w') # r - open if already present(default) w- also create  a- append data
# f.write("Hi soham")
# f.close()
# f = open('soham.txt','a') # r - open if already present(default) w- also create  a- append data
# f.write(" appending text")
# f.close()
# f = open('soham.txt')
# print(f.read())


# my_dict={'name':'Soham'}
# print(my_dict['names']) #KeyError
#
# my_list = [23,45,66,88,58]
# my_list.remove(45)
# my_list.remove(45) #ValueError
# print(my_list)
# my_list.delete(66) #AttributeError
# print(my_tuple) #NameError
a = 45 #int
b = '35' #str
# add = a+b
# print(add) #TypeError

# r
# R
# Rock
class NewError(Exception):
    pass

my_list = [23,45,66,88,58]
my_list.remove(45)
try:
    if 45 not in my_list:
        raise NewError
    my_list.remove(45)
    print('Removed successfully')
except NewError:
    print('Item already removed')
print(my_list)

