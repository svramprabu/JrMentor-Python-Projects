# HW

# Declare variable as name, class, age and date of birth
# get value from the user and store in respective data types and
# print the same in a single line seperated by *
# print a new line atlast

# a = 7 #'selva'
# b = 2 #'raj'
# print(a+b)
# a = {1,2,3}
# b = {1,2}
# print(a**b)
# print(a!=b)
# a/=1
# print(a)
# print(b>a and a>b)
# print(not False)
# get user input 1. first name 2. last name
# concat and print 3rd letter of first name and
# 1st letter of last name

# bitwise and
# a = 1
# b = 1
# print(~ b)

# your_age_is = 17
# print(f'Your Age is {your_age_is}')
# print(45 & 28)
# print(36|97)
# y = [1,2,3,4,5,6]
# x = 2
# print(x not in y)
# def room1():
#     a = 10
#     return a
# a = room1()
# print(a)

# a = int(input('Enter a no'))
# if (a<99):
#     print('Condition is true')
# elif (a==100):
#     print('Given no is 100')
# elif (a==101):
#     print('Given no is 101')
# else:
#     print('Condition is false')

# print('selva'in'rajselva')

# list_of_subjects=['maths','eng','tam','phy','chem']
# print(list_of_subjects)
# for each_subject in list_of_subjects:
#     print(each_subject)
#
# alphabets='abcdefghijklm'
# for each_alphabet in alphabets:
#     print(each_alphabet)

# Multiplication Tables
# table_no = int(input('Enter the table no of your choice: '))
# for each in range(1,11):
#     ans=each*table_no
#     print(f'{each} x {table_no} = {ans}')

# for 3 tries check password

# i = 1
# while(i<10):
#     print(i)
#     i+=1 #i=i+1

# saved_password = 'selvaraj123'
# user_password=''
# while(saved_password != user_password):
#     user_password=input('Enter the right password')
#     if (user_password==saved_password):
#         print('Success')
#     elif ('selva' in user_password):
#         print('Semi correct')
#     else:
#         print('Try again')

# user_limit = input('Do you wan to play Y/N')
# while(user_limit=='Y'):
#
#     p1=r,s,p
#     p2
#     if (p1=='r' and p2=='s'):
#         print('p1 wins')
#     elif ()
#
#
#     else:
#         print('invalid input')
#     user_limit = input('Do you wish to play again? Y/N')

# def doublePlayer():
#     for i in range(10):
#         if i == 4:
#             # break
#             # continue
#             pass
#         print(i)

# def singlePlayer():
#     import random
#
#     options=['r','p','s']
#     com = random.choice(options)
#     print(com)


# singlePlayer()

# def function2():
#     a = 'great'
#     return a
#
# print(function2())
# ans = function2()
# print(ans)
#
# def additionFn(a,b):
#     print(a+b)
#
# additionFn(1,2)
#
# def subtraction(a,b):
#     return a-b
#
# a = 5
# b = 3
# print(subtraction(a,b))

# import dhruv
# from MyOwn import test_pack

# list_of_list = [[1,2,3],['a','b','c'],[12.1,15.6]]
# print(list_of_list)
# print(list_of_list[0][0])
# print(list_of_list[1])

# List = ['Like','Dislike']
# Tuple = (1,2,33,5)
# # print(Tuple)
# Dict = {'Likes':241,'Dislikes':23424}
# print(Dict['Like'])
# [123,12344]
# Tuple[0]=5
# print(List[1])
# List[1]='svr'
# print(List)


# Story Generator
# name = input('Enter your name')
# place = input('Enter your fav place')
# animal = input('Your fav animal')
# month = input('Your fav month of the year')
# talent = input("what's your natural talent?")
# person = input("Who's your fav person")
#
# print(f"""Hi I'm {name} I'm coming from {place} and {animal}
# can be seen all over my {place} during
# the every {month} and these {animal}s taught {person} how to {talent}""" )


# from packageforSadhya import module1
# module1.fn1()

# dice simulator

# import random
# dice = [1,2,3,4,5,6]
# user_option = input('Do you wish to roll the dice? y/n')
# while (user_option == 'y'):
#     result = random.choice(dice)
#     print(f'After rolling you got {result}')
#     user_option = input('Do you wish to roll the dice again? y/n')

# def checkPrime(number):
#     for i in range(2,number):
#         if (number % i == 0):
#             return 'not prime'
#     return 'prime number'
#
# n = int(input('enter a no'))
# print(checkPrime(n))

# prime_no = 1 #flag variable
# n = int(input('enter a no'))
# for i in range(2,n):
#     if (n % i == 0):
#         prime_no=0
#
# if prime_no==1:
#     print('prime number')
# else:
#     print('not prime')


# user_data = input('enter data').split()
# print(user_data)
# ans = ''
# for each in user_data:
#     ans = ans+each[0]
#     print(ans)
# print(ans.upper())

# list_of_nos = input('Enter few nos').split()
# even = []
# odd = []
#
# for each_no in list_of_nos:
#     if int(each_no) % 2 == 0:
#         even.append(each_no)
#     else:
#         odd.append(each_no)
#
# print('Even list: ',even)
# print('Odd list: ',odd)

# Number guessing game
# import random
#
# com = random.randint(1,100)
# user = int(input('Choose and enter a number between 1 and 100'))
# attempts = 0
#
# while(True):
#     if (user > com):
#         print('try with a smaller number')
#         attempts+=1
#         user = int(input('Enter here: '))
#     elif (user < com):
#         print('Try with a bigger number')
#         attempts+=1
#         user = int(input('Enter here'))
#     else:
#         print(f'You found the number in {attempts}')
#         break
# print('Thank you for playing')

# Word guessing game

# import random #step 1
# list_of_words = ['selvaraj','ramprabu'] #step 1
# choice = random.choice(list_of_words) #step 2
# attempts = 5 #step 3
# print(len(choice),'is the length of the word you have to guess') #step 3
# guess=[] #step 3
# onscreen = ''
#
# while(attempts > 0): #step 4
#     onscreen = ''
#     for each_char in choice: #step 7
#         if each_char in guess:
#             onscreen += each_char
#         else:
#             onscreen += '_'
#         # print(onscreen)
#
#     print(onscreen)
#     print(f'you have {attempts} left')
#     # break
#     user_letter = input('enter a letter').lower() #step 5
#     if user_letter in choice: #step 6
#         guess.append(user_letter)
#         attempts-=1
#         print(f'{user_letter} is present in the word')
#
#     else:
#         print(f'{user_letter} is not in the word')
#         attempts-=1
#
# if (attempts == 0 ): #step 8
#     if onscreen == choice:
#         print('Won the game')
#     else:
#         print('you lost')

# x = [[1,2,3],[4,5,6],[7,8,9]]
# print(x)

# for i in x:
#     for j in i:
#         print(i,j)
# for i in range(len(x)):
#     for j in range(len(x[i])):
#         print(i,j,'=',x[i][j])
# print(i)

# print('*****\n****\n***\n**\n*')

# number = int(input('Enter the no: '))

# for each_row in range(number): #[0,1,2,3,4]
#     for each_col in range(number-each_row): #[5,4,3,2,1]
#         print('*',end='')
#     print()


# for i in x: #x is a sequence

# for i in range(x) #x is a number

# print('* * * * *\n * * * *\n  * * *\n   * *\n    *')

# n=5
# for each_row in range(n): #0,1,2,3,4
#     for each_col in range(each_row): #0,1,2,3,4
#         print(' ',end='') #
#     for each_col in range(n-each_row): #5,4,3,2,1
#         print('* ',end='')
#     print()

# To check string is palindrome

# method 1
# s1 = 'Selvaraj'  # input('s1: ')
# s2 = ''
# for each_char in s1:
#     s2 = each_char + s2  # 1: S+'' 2: e+S 3: l+eS 4: .....
#     print(s2)
# if s1 == s2:
#     print('palindrome')
# else:
#     print('not a palindrome')

# method 2
# String slicing
# print(s1[::-1])  # s1[0] s1[0+1] s2[0+1+1]
# string[start:end:step]
# print(s1[-2])

# s1 = 'Selvaraj'  # input('s1: ')
# s2 = s1[::-1]
# if s1 == s2:
#     print('palindrome')
# else:
#     print('not a palindrome')

# method 3
# s1 = 'Python'
# s2 = []
# print(len(s1))
# # for i in range(8):
# for i in range(len(s1)):  # [0,1,2,3,4,5,6,7]
#     s2.append(s1[-1 - i])  # -1 -2 -3 -4 -5
# print(s2)
# s2 = ''.join(s2)
# print(s2)
# if s1 == s2:
#     print('palindrome')
# else:
#     print('not a palindrome')

# f = open('selva.txt') #throws error
# f = open('selva.txt','w')
# f.write('Selva is in his Higher secondary\n')
# f.write('Hackerkid\n')
#
# f=open('selva.txt','a')
# f.write('Appending data\n')
#
# f.close()
#
# f=open('selva.txt')
# print(f.read())

# try:
#     f = open('sr.txt')
# except:
#     print('File not found or file name error')


def selva():
    pass
selva()