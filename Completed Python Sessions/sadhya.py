# a = 1
# print(a) #this line prints the value of a
# print(type(a))
#
# b = 2.9
# print(b)
# print(type(b))

# a = 1
# b = 2
# print(a,b,sep='$')
# print(a,end='------')
# print(b,end='')

# write a python program to get
# user's name and date of birth
#  and print them by using * as a seperator
# and use >>> as an end argument

# user_name = input('Enter your name: ')
# date_of_birth = input('Enter your DOB: ')
# print(user_name,date_of_birth,sep='*',end='>>>')

# a = 3   #input('enter a number')
# b = 2   #input('enter another number')
# print(a != b)

# print(False and False)

# num = int(input('Enter a number: '))
# if (num<20):
#     print('Yes')
# elif (num==20):
#     print('20')
# else:
#     print('No')

# saved_password = 'sadhya123'
# user_password = input('Enter the password')
# if (user_password == saved_password):
#     print('Success')
# else:
#     print('Failure, wrong password')

# toys = ['cycle','bike','barbie','teddy']
# print(toys)
# for i in toys:
#     print(i)

# i = 1
# while i<1000:
#     print(i)
#     i+=1 #i=i+1

    # # 1st iteration or 1st cycle
    # i = 1
    # 1<10
    # print(1)
    # i+=1 -> i = i+1 -> i = 1+1 -> i=2
    # #2nd iteration
    # i=2
    # 2<10
    # print(2)
    # i = 3
    # 3rd
    # 4th
    # 5th
    # ..
    # .
    # i=10

# saved_password = 'sadhya123'
# user_password = ''
# while(saved_password != user_password):
#     user_password = input('Enter the correct password')
#     if ('vishwa' in user_password):
#         print('Sorry vishwa better luck next time')
#         break
#     if (user_password==saved_password):
#         print('success')

# user_input = input('Enter something')
# if (user_input=='sadhya'):
#     print(user_input)
# else:
#     pass
    # print(user_input)

# while (1<2):
#     pass

# a = 5
# print(a)
# print('=',a)
# print(f'= {i*table_number}') #add f at the beginning of the string and add curly bracket around the variable

# x = 10
# y = 20
# def addition(a,b):
#     return a+b
# print(addition(x,y))
# print(addition(23,1234))

# print("""Once, there lived a animal1 in the dense and lively place.
# The animal1 was known for his talent and was loved by name.
# One day, a animal2 unfortunately ran over the animal1’s tail.
# The animal1 awakened abruptly, trapping the animal2 under his massive paw.""")

# from packageforSadhya import module1
# module1.fn1()

# my_list = [1,2,3,4,5]
# my_tuple = (1,2,3,4,5)
# print(my_list)
# my_list[0]=123 #mutable
# print(my_list)
# my_tuple[0]=123 #immutable

# import random
# dice = [1,2,3,4,5,6]
# user_option = input('Do you wish to roll? y/n').lower()
# while (user_option == 'y'):
#     answer = random.choice(dice)
#     print(f'You got {answer} by rolling the dice')
#     user_option =input('do you wish to roll again? y/n').lower()

# Find even and odd numbers from a list, and store them separately in a new list
# list_of_numbers = input('Enter the numbers').split()
# even_list=[]
# odd_list=[]
#
# for each_number in list_of_numbers:
#     if (int(each_number) % 2 == 0):
#         even_list.append(each_number)
#     else:
#         odd_list.append(each_number)
#
# print('Even List: ',even_list)
# print('Odd List: ',odd_list)

# student_name = input('Enter your name')
# eng_mark = int(input('Enter English marks'))
# tel_mark = int(input('Enter Telugu marks'))
# math_mark = int(input('Enter Maths marks'))
# sci_mark = int(input('Enter Science marks'))
# soc_mark = int(input('Enter Social marks'))
#
# total_marks = eng_mark + tel_mark + math_mark + sci_mark + soc_mark
#
# print(f'Hi {student_name}')
# print(f"""
# you scored
# {eng_mark}/100 in English
# {tel_mark}/100 in Telugu
# {math_mark}/100 in Maths
# {sci_mark}/100 in Science
# {soc_mark}/100 in Social
#
# And your total marks is {total_marks}/500
# """)

# Find whether the number is prime or not
# def primeornot(number):
#     for i in range(2, number):
#         if (number % i == 0):
#             return('not a prime number')
#     return('prime number')
#
# number = int(input('enter the number'))
# print(primeornot(number))

# def add():
#     a = int(input('a = '))
#     b = int(input('b = '))
#     ans = a+b
#     print(f"{a}+{b}={ans}")
#
# def sub():
#     a = int(input('a = '))
#     b = int(input('b = '))
#     ans = a-b
#     print(f"{a}-{b}={ans}")
#
# def mul():
#     a = int(input('a = '))
#     b = int(input('b = '))
#     ans = a*b
#     print(f"{a}*{b}={ans}")
#
# def div():
#     a = int(input('a = '))
#     b = int(input('b = '))
#     ans = a/b
#     print(f"{a}/{b}={ans}")
#
# print('Welcome to my calculator app in Completed Python Sessions')
# while(True):
#     user_option = int(input("Available options are \n1.add \n2.sub \n3.mul \n4.div\n5.exit\nyour option: "))
#     if (user_option == 1):
#         print('You have chosen add')
#         add()
#     elif (user_option == 2):
#         print('You have chosen sub')
#         sub()
#     elif (user_option == 3):
#         print('You have chosen mul')
#         mul()
#     elif (user_option == 4):
#         print('You have chosen div')
#         div()
#     elif (user_option == 5):
#         print('Thank you for using my application')
#         break
#     else:
#         print('Invalid Input try again')
#         continue

# Adding items to a list
# [item1,item2,item3]

# student names list

# step 1
# student_name_list = [] #declaring empty list
# number_of_students = int(input('Enter the number of students')) #asking for number of students
#
# # step 2
# for i in range(number_of_students): #run the loop to collect name
#     student_name = input('Student name: ') #getting the name
#     student_name_list.append(student_name) #add it to the list
#
# # step 3
# print('Name list: ',student_name_list) #printing the list



# Target --> [{name:sadhya,eng:,tel:},{},{}]
# Student detail program 2
# student_name_list = []
# def add_detail():
#     student_dict = {}
#
#     student_name = input('Enter the student name: ')
#     student_dict['name']=student_name #{name:sadhya}
#
#     eng = int(input('English marks: '))
#     student_dict['english'] = eng
#
#     tel = int(input('Telugu marks: '))
#     student_dict['telugu'] = tel
#
#     student_name_list.append(student_dict)
# def view_list():
#     for i in student_name_list:
#         print('--->',i)
#
#
# while(True):
#     option = int(input('\n1.Add a student detail\n2.View list\n3.Exit\noption: '))
#     if option == 1:
#         add_detail()
#     elif option == 2:
#         view_list()
#     elif option == 3:
#         break
#     else:
#         print('Wrong option choose correctly')
#         continue

# Todo list of tasks
# add a task
# remove a task
# search a task
# view all tasks
# number of tasks
# exit

# list_of_tasks = []
# while(True):
#     user_option = int(input('\nChoose an option to do the respective'
#                             ' \n1.Add a task'
#                              '\n2.Remove a task'
#                             '\n3.Search a task'
#                             '\n4.View all tasks'
#                              '\n5.number of tasks\n6.Exit\n: '))
#     if (user_option == 1):
#         task = input('Enter the name of the task: ')
#         list_of_tasks.append(task)
#         print('Task added successfully')
#     elif (user_option == 2):
#         task = input('Enter the task to be removed: ')
#         if task in list_of_tasks:
#             list_of_tasks.remove(task)
#             print('Task removed successfully')
#         else:
#             print('Task is not present in the list')
#     elif (user_option == 3):
#         task = input('Enter the task to search: ')
#         if task in list_of_tasks:
#             print('Task is present in the list')
#         else:
#             print('Task is not present in the list')
#     elif (user_option == 4):
#         print('List of tasks:')
#         for each_task in list_of_tasks:
#             print('-',each_task)
#     elif (user_option == 5):
#         numer_of_tasks = len(list_of_tasks)
#         print(f'There are {numer_of_tasks} tasks in the list')
#     elif (user_option == 6):
#         print('Thank you for using the application')
#         break
#     else:
#         print('wrong option try again')
#         continue

# Password generator
# length -> 1 uppercase, 1 symbol, 1 number and remaining all lowercase characters
#
# import random
# upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# lower = 'abcdefghijklmnopqrstuvwxyz'
# numbers = '0123456789'
# symbols = '!@#$%^&*'
#
# pass_len = int(input('Length of the password: ')) #length
#
# password = '' #answer variable
#
# password += password.join(random.sample(upper,1))
# password += password.join(random.sample(symbols,1)) #1. random picking 2. list to string 3. adding it to answer var
# password += password.join(random.sample(numbers,1))
# password += ''.join(random.sample(lower,pass_len-3)) #['e','i','o'] -> eio -> add to ans var
# # print()
#
# print(password)

f = open('sadhya.txt','w')
f.write("Hi I have finished python basics\n")
f.close()

f = open('sadhya.txt')
print(f.read())