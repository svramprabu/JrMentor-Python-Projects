# "Declare a var and store all lower case alphabets as a string
# print the vowels (a,e,i,o,u) using string access
# print a,e,i using positive indexing and o, u using negative indexing"
# alp="abcdefghijklmnopqrstuvwxyz"
# print(alp)
# print("The vowels are:")
# print(alp[0]) #a
# print(alp[4]) #e
# print(alp[8]) #i
# print(alp[-12]) #o
# print(alp[-6]) #u

# Different methods available in a list
# eg_list = [45,49,47,48]
#
# # to access an item in the list
# print(eg_list[0])
# # to add a new item to the list
# eg_list.append(50)
# print(eg_list)
# # to remove an item from the list
# eg_list.remove(49)
# print(eg_list)
# # to find the minimum of the list
# print(min(eg_list))
# # to find the maximum of the list
# print(max(eg_list))
# # to find the sum of elements
# print(sum(eg_list))
# # to find the no of items in a list
# print(len(eg_list))

# a = 10
# b = 12.5
# sum = a+b
# print(sum)

# Explicit type conversion
# a =
# int(a)
# float(a)
# str(a)

# a = 10
# b = '12'
# b = int(b)
# sum = a+b
# print(sum)

# a = 123
# b = 123.45
# c = "abcd"

# print(a,b,c)

# d = input('Your question here')
# print(d)
# print(type(d))
#
# e = int(input('your age'))
# print(e)
# print(type(e))
#
# f = float(input('your weight'))
# print(f)
# print(type(f))

# print(a,b,c)
# print(a,b,c,sep='--->')
# print(a,sep='--->')
# print(a,end='$$$')
# print()

# x = 11
# y = 2
# print('x+y=',x + y)
# a = 'Python'
# b = 'Programming'
# print('a+b=',a + b) #concatenation

# print('x-y=',x - y)
# print('x*y=',x * y)
# print('x/y=',x / y)
# print('x%y=',x % y) #remainder
# print('x//y=',x // y) #quotient

# x = int(input('Enter a number: '))
# y = int(input('Enter a number: '))
# add = x + y
# print('x+y=',add)

# Take input from user collecting marks in different subject
# 5 subjects
# output total marks

# print('Total marks',add,'in the mid term ')

# n = input('Name: ')
# a = int(input('age: '))
# l = input('location: ')
# print('Hi my name is',n,'I am ',a,'years old','I am from',l)
# print(f"Hi my name is {n} I am {a} yeras old and I'm from {l}")

# > greater than
# print('5 > 3 =',5>3)
# print('3 > 5 =',3>5)

# < less than
# print('3 < 5 =',3<5)
# print('5 < 3 =',5<3)

# == value equals
# print('3 == 3',3==3)
# print('3 == 5',3==5)

# != value not equals
# print('3 != 5',3!=5)
# print('3 != 3',3!=3)

# >= greater than or equals
# print('5 >= 3',5>=3)
# print('5 >= 5',5>=5)
# print('3 >= 5',3>=5)

# <= lesser than or equals
# print('3 <= 5',3<=5)
# print('5 <= 5',5<=5)
# print('5 <= 3',5<=3)

# take input from the user asking for his/her birth year
#     calculate the age using that and print a statement
# that says "As your were born in 1994 your age is 30"

# take 4 inputs
# input 1 name and input 2 height
# input 3 name and input 4 height
# difference in heights
# "person1 is taller than person2 by x cms"

# name1 = input('Name of person 1: ')
# name2 = input('Name of person 2: ')
# height1 = float(input('Height of person 1: '))
# height2 = float(input('Height of person 2: '))
#
# print(f'Difference between the heights of {name1} and {name2} is {height1-height2}')

# age = int(input('Age: '))
# print(f"Your age is {age>0}")

# a = 123

# += Arithmetic and assignment -> compound operator
# a += 10 # a+10 -> a = a+10
# print(a)

# count = 100
# count -= 1 #count = count - 1

# b = 13
# b *= 3
# print(b)
#
# a = 10
# a //= 5

# if (5 > 3):
#     print('Five is greater than three')

# declare two variables get input and check if first var is
# greater than second and print something based on that

# a = int(input('a='))
# b = int(input('b='))
# if(a>b):
#     print('A is greater than B')


# HW get the age of a person and your print if he's
# eligible for voting

# a = int(input('a='))
# b = int(input('b='))
# if(a>b):
#     print('A is greater than B')
# else:
#     print('A is not greater than B')

# a = int(input('a='))
# b = int(input('b='))
# if(a>b):
#     print('A is greater than B')
# elif (b>a):
#     print('A is not greater than B')
# else:
#     print('A is equal to B')

# age = int(input('Age: '))
# if (age < 5):
#     print('KG')
# elif (age<10):
#     print('Primary')
# elif (age < 16):
#     print('Secondary')
# elif (age < 18):
#     print('Higher secondary')
# else:
#     print('the person is of over age')

# Rock Paper Scissors

# print('Welcome to my Rock Paper Scissors Game\n')
# p1 = input('Enter Rock(r) or Paper(p) Scissors(s): ').lower()[0]
# p2 = input('Enter Rock(r) or Paper(p) Scissors(s): ').lower()[0]
#
# if (p1 == 'r' and p2 == 'p'):
#     print('Player 2 wins')
# elif (p1 == 'p' and p2 == 'r'):
#     print('Player 1 wins')
# elif (p1 == 's' and p2 == 'r'):
#     print('Player 2 wins')
# elif (p1 == 'r' and p2 == 's'):
#     print('Player 1 wins')
# elif (p1 == 'p' and p2 == 's'):
#     print('Player 2 wins')
# elif (p1 == 's' and p2 == 'p'):
#     print('Player 1 wins')
# elif (p1 == p2): #p p r r s s
#     print('It is a Tie')
# else:
#     print('Invalid input')

# a=[12,13,14,15,16]

# if a[0]%2==0:
#     print('even')
# else:
#     print('odd')
# if a[1]%2==0:
#     print('even')
# else:
#     print('odd')

# a=[12,13,14,15,16]
# for i in a:
#     print(i)

# a=[12,13,14,15,16]
# for i in a:
#     if (i % 2 == 0):
#         print('Even')
#     else:
#         print('Odd')

# s = 'Python Programming'
# for i in s:
#     print(i)

# s = input('Enter a para: ').split()
# # print(s)
# for each_word in s:
#     print(each_word)

# Acronym generator
# US -> United States
# step 1 split
# step 2 string access the first letter
# step 3 concat all of these and store in ans variable

# text = input('Enter the abbreviated text: ') #step 1
# s = text.split()
# ans = ''
# for each_word in s:
#     ans += each_word[0] # -> U -> U + S -> US
#     # print(each_word[0])
# print(f"Acronym generated for {text} is {ans}")

# my_list = [1,2,3,4]
# marks = []
# for i in range(5):
#     # print(123)
#     mark = int(input('Enter the mark: '))
#     marks.append(mark)
# print(marks)

# f string, for loop, range
# 1 X 5 = 5
# table_no = int(input('Table no: '))
# for i in range(1,11):
#     print(f'{i} X {table_no} = {i*table_no}')

# letter = input('Enter the letter: ')
# string = input('enter the Sentence: ')
# count_of_letter = 0
# for each in string:
#     if (each == letter):
#         count_of_letter += 1
# print(f'Number of times the letter {letter} has occured in the '
#         f"sentence '{string}' is {count_of_letter}")

# number = int(input('Enter a number: '))
# number = str(number)
# no_of_digits = len(number)
# print(f'The number of digits in {number} is {no_of_digits}')

# i = 1
# while (i<10):
#     print(i)
#     i += 1

# number = int(input('Enter a number: ')) #12345 -> 5
# no_of_digits = 0
# while(number > 0):
#     remainder = number % 10 #5
#     number = number // 10 #12345 1234 123 12 1 0
#     no_of_digits += 1
#     print(remainder)
#     print(number)
# print(f'The number of digits is {no_of_digits}')

# saved_password = 'pass123'
# user_password = ''
# while(saved_password != user_password):
#     user_password = input('Enter password: ')
#     if (saved_password == user_password):
#         print('Success')
#     else:
#         print('Try again')


# Height and Weight
# 160cms and 90kgs
# allowed

# height = int(input('Enter height: '))
# weight = float(input('Enter weight: '))
# if (height >= 160):
#     if (weight <= 90):
#         print('Allowed to ride')
#     else:
#         print('He is overweight')
# else:
#     print('He is short even to try')

# saved_password = 'pass123'
# user_password = ''
# while(saved_password != user_password):
#     user_password = input('Enter password: ')
#     if (saved_password == user_password):
#         print('Success')
#     else:
#         if ('pass' in user_password):
#             print('Semi correct')
#         else:
#             print('Try again')

# x = [[4,5,6],'Nested List']
# for i in x:
#     for j in i:
#         print(j)

# * * *
# * * *
# * * *

# n = int(input('Enter value of n: '))
# for i in range(n):
#     for j in range(n):
#         print('* ',end='')
#     print()

# *
# **
# ***
# ****
# *****

# n = 5 #int(input('Enter value of n: '))
# for i in range(n):
#     for j in range(i+1): # 1 2 3 4 5
#         print('* ',end='')
#     print()

# ***
# **
# *

# n = 5
# for i in range(n):
#     for j in range(n-i):
#         print('*',end='')
#     print()

# 1
# 2 2
# 3 3 3
# 4 4 4 4

# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(str(i+1)+' ',end='')
#     print()

#     *
#    * *
#   * * *
#  * * * *
# * * * * *

# n = 5
# for i in range(n):
#     for j in range(n-i-1): #4 3 2 1 0
#         print(' ',end='')
#     for j in range(i+1):
#         print('* ',end='')
#     print()

# for i in range(10):
#     if i == 4:
#         continue
#     print(i)

# saved_password = 'pass123'
# count = 0
# while(True):
#     user_password = input('Enter password: ')
#     if (saved_password == user_password):
#         print('Success')
#         break
#     else:
#         count+=1
#         if count == 3:
#             print('Out of attempts')
#         else:
#             print('Try again')
#             continue
#         print(f'No of attempts {count}')

# Task manager application

def addTask():
    print('Lets add a task')
    task = input('Task name: ')
    if task in list_of_tasks:
        print('Task already present\n')

    else:
        list_of_tasks.append(task)
        print('Task added successfully\n')

def remTask():
    print('To delete a task')
    task = input('Enter the task name: ')
    if task in list_of_tasks:
        list_of_tasks.remove(task)
        return ('Task deleted successfully\n')
    else:
        return ('Task is not present in the list\n')


print('Welcome to my task manager application')
list_of_tasks = []

while(True):
    user_option = int(input('1.Add a task\n'
                            '2.Remove a task\n'
                            '3.Search\n'
                            '4.Print\n'
                            '5.Number of tasks\n'
                            '6.Exit\n'
                            'Choice: '))
    if (user_option == 1):
        addTask()
    elif(user_option == 2):
        print(remTask())
    elif (user_option == 3):
        task = input('Enter task to search: ')
        print('Searching....')
        if task in list_of_tasks:
            print('Task found\n')
        else:
            print('Task not found\n')
    elif (user_option == 4):
        print('Tasks available are')
        for each in list_of_tasks:
            print(f"- {each}")
        print()
    elif (user_option == 5):
        print(f"The number of tasks: {len(list_of_tasks)}\n")
    elif (user_option == 6):
        print('Thank you for using my application')
        break
    else:
        print('Invalid input')

# def function(): #parameters or arguments
#     print('Hiiiii')
#     # return ...
#
# function() #fnuction calling

# print('Hiii') #Hiii is the argument
# a = input('a=')
# print(a)
#
# print(input('input: '))

# arg n ret
# Type 1 no arg n no return
# def task_manage():
#     print('OKK')
# task_manage()

# def pattern():
#     n = 5
#     for i in range(n):
#         for j in range(n-i-1):
#             print(' ',end='')
#         for j in range(i+1):
#             print('* ',end='')
#         print()
#
# pattern()

# Type 2 function no argument but a return

# def func():
#     a = input('first name: ')
#     b = input('last name: ')
#     add = a+b
#     return add
# a = func()
# print(a)
#
# print(func())

# Type 3 no return but has argument
# def func2(a,b):
#     add = a+b
#     print(add)
#
# a = input('first name: ')
# b = input('last name: ')
#
# func2(a,b) #pass by reference
# func2('Ramprabu','S V') #pass by value

# Type 4 both argument n return are present

def func4(x,y):
    return x*y

print(func4(5,4))


