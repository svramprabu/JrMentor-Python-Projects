# a = 'vishnu123'
# b = input('Enter password')
# if a==b:
#     print('ok')
# else:
#     print('not')
# courses = 'ramprabu'
# for each_course in courses:
#     print(each_course)

# var = 25
# while var > 15:
#     var -=1
#     if var == 20:
#         continue
#     print(f'the value is {var}')
# import random

# player_1 = input('Enter Rock(R) or Paper(P) or Scissor(S)')

# computer_input = ['R','P','S']
# print(random.choice(computer_input))
# player_2 = random.choice(computer_input)
# player_2 = input('Enter Rock(R) or Paper(P) or Scissor(S)')
#
# if (player_1=='R' and player_2=='S'):
#     print('player 1 wins')
# elif (player_1=='S' and player_2=='R'):
#     print('player_2 wins')
# elif (player_1=='R' and player_2=='P'):
#     print('player 2 wins')


# import random
#
# user_choice = input('Single(S) or Double Player(D)').upper()
# if user_choice=='S':
#     print('Single player mode')
#     options = ['R', 'P', 'S']
#     player = None
#     com = random.choice(options)
#
#     player = input('Enter Rock(R) or Paper(P) or Scissor(S):').upper()
#     print(f" computer choose {com}")
#     print(f"player choose {player}")
#     if player == 'R' and com == 'P':
#         print('You lose')
#     elif player == 'P' and com == 'R':
#         print('You win')
#     elif player == 'S' and com == 'R':
#         print('You lose')
#     elif player == 'R' and com == 'S':
#         print('you win')
#     elif player == 'P' and com == 'S':
#         print('You lose')
#     elif player == 'S' and com == 'P':
#         print('You win')
#     else:
#         print('Tie')
#
# elif user_choice=='D':
#     print('Double player mode')
#
# else:
#     print('sorry wrong input')


# def addNumbers(a,b):
#     print(a+b)
#
#     # print(c)
#
# addNumbers(1,2)
# addNumbers(3,5)
# addNumbers(9,213)

# Completed Python Sessions Program To Convert Fahrenheit to Celsius
# def TemperatureConvertion(Fahrenheit):
#     Celcius = ((Fahrenheit-32)*5)/9
#     # return Celcius
#     print(Celcius)
#
# TemperatureConvertion(233)

# BMI Calculator with Completed Python Sessions
# [weight (kg) / height (cm) / height (cm)] x 10,000
# (wgt/(hgt*hgt))*10000

# def fn1():
#     x = 10 #local var
#     def fn2():
#         y = 15 #non local
#         print(y)
#         print(x)
#     print(y)

# # Print the multiplication table
# table_no = int(input('enter the table no: '))
# for i in range(1,11):
#     print(f'{i} x {table_no} = {i * table_no}')
    # print(i*table_no)

# list_of_items = ['vishnu','ganesh']
# list_of_items = [] #step 1
# # while ()
# list_of_items.append(input('Enter the item'))

# from MyOwn import test_pack
# testFn()

# Indian Space Research Organisation
# ISRO

# # even or odd
# list_of_nos = input('enter few nos').split()
# even_list=[]
# odd_list=[]
#
# for each_no in list_of_nos:
#     if (int(each_no) % 2 == 0):
#         even_list.append(each_no)
#     else:
#         odd_list.append(each_no)
# print(even_list)
# print(odd_list)

# Student report card
# name = input('Name: ')
# math_marks = int(input('Math marks: '))
# sci_marks = int(input('Science marks: '))
# soc_marks = int(input('Social marks: '))
# total_marks = math_marks + sci_marks + soc_marks
#
# print(f"""
# Hi, {name}
# Maths marks: {math_marks}
# Science marks: {sci_marks}
# Social marks: {soc_marks}
# Your total marks is {total_marks}/300 """)

#guess the word
# Step 1 computer assumes a word
# import random
# list_of_words = ['python','programming','hackerkid']
# com = random.choice(list_of_words)
# guess = []
# word_on_screen = ''
# attempts = 10
#
# while(attempts > 0):
#     # step 2 resultant word with dashes
#     word_on_screen = ''
#     for each_letter in com:
#         if each_letter in guess:
#             word_on_screen += each_letter
#         else:
#             word_on_screen += '_'
#     print(word_on_screen)
#
#     # step 5 closing with success
#     if word_on_screen == com:
#         print('You found the answer')
#         break
#
#     # step 3 get user input for a letter
#     print(f'you have {attempts} attempts left')
#     user_input = input('Choose a possible letter: ').lower()
#     if user_input in com:
#         print(user_input,'is in the word')
#     else:
#         print(user_input,'is not in the word')
#     guess.append(user_input)
#
#     # step 4
#     attempts -= 1
#
# # step 6 after coming out of while loop
# if attempts == 0:
#     if word_on_screen == com:
#         print('You found the word')
#     else:
#         print('Try again later')

# print(5+'10')
# x = {1:123}
# print(x[12])

# a = [1,2,3,4]
# try:
#     print(a[1])
#     print(a[5])
# except:
#     print('error occured')

# tasks =[]
# def add_task(task):
#     tasks.append(task)
#     print(f'{task} has been added')
#
# def del_task(task):
#     if task in tasks:
#         tasks.remove(task)
#         print(f"{task} has been removed")
#
# def view_tasks():
#     for each_task in tasks:
#         print('-',each_task)
#
# print('My todo list program')
# while(True):
#     option = int(input('\n1.add task\n2.del task\n3.view task\n4.exit\nyour option: '))
#     if (option == 1):
#         task = input('enter a task in mind: ')
#         add_task(task)
#     elif (option == 2):
#         task = input('enter a task in mind to delete: ')
#         del_task(task)
#     elif (option == 3):
#         view_tasks()
#     elif (option == 4):
#         print('thank you')
#         break


# Password Generator program

# import random
# pass_len = int(input('password length: '))
# sample = 'ABCabc012!@#'
# print(''.join(random.sample(sample,pass_len)))

# Nested for loop
# bucket_list = [[1,2,3],[4,5,6],[7,8,9]]
# for each_item in bucket_list:
#     print(each_item)
#     for each in each_item:
#         print(each)

# print('*****\n****\n***\n**\n*')

# number = 5
# for i in range(number): #[0,1,2,3,4]
#     for j in range(number): #[5,4,3,2,1]
#         print('*',end='')
#     # break
#     print()

print('* * * * *\n * * * *\n  * * *\n   * *\n    *')
number = 5
for i in range(number):
    for j in range(i):
        print(' ',end='')
    for k in range(number-i):
        print('* ',end='')
    print()
