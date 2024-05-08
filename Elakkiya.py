# elakiya = 1
# print(elakiya)

# (int,float,str,bool)

# 1 - int
# 2.3 - float
# 2.5 - float
# 7 - int
# 'hiii' - str
# 5.9 - float
# '5.9' - str
# '3' - str

# a = '1.5'
# print(a)
# print(type(a))

# 0 based indexing
# alphabets = 'abcdefghijklmnopqrstuvwxyz'
# vowels = a e i o u
# print(alphabets)
# print(alphabets[0])        # we are printing a here
# print(alphabets[4])         # we are printing e here
# print(alphabets[8])
# print(alphabets[14])
# print(alphabets[20])

# how to get user input

# a = input('What is your name? ')
# print(a)
#
# b = input('What is your age?')
# print(b)
# # print(a,b,sep='/')
# print(a,end='-----')
# print(b,end='\n')
# print(a,b,sep='',end='')
#arguments

# declare variables and collect user name and phone number
# print them using & as seperator and finally end with a dollar symbol $

# first_number = int(input('Give first number')) # getting  no and storing as integer
# second_number = int(input('Give second number'))
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a**b)
# print(a%b)
# print(first_number,second_number)

# x = 5
# y = 7
# print(True or True)
# print(not False)
# 2 0001101010 convert to binary ----- decimal
# 3 0100010110

# List_of_toys = ['cycle','ball','band']
# print('ball'not in List_of_toys)

# == or is
# x = 5
# y = 5
# print(x is not y)

# test_number = int(input('Enter a number'))
# if (test_number>10):
#     print('test number is greater that 10')
# elif (test_number==10):
#     print('the number is 10')
# else:
#     print('test number is less than 10')


# user_input height as int
# if height is greater than 100 print goto ride 1
# if height is equal to 100 print goto ride 2
# else print goto ride3

# makeup_items = ['clips','hairpins','brush','comb']
# print(makeup_items)
# for i in makeup_items:
#     print(i)
#
# i = 0
# while (i<10):
#     print(i)
#     i=i+1

# saved_password = 'elakiya123'
# user_password = ''
# while (saved_password != user_password):
#     user_password = input('Enter the right password: ')
#     if (user_password==saved_password):
#         print('Success')
#     else:
#         print('Retry')

# for x in range(10):
#     if x == 5:
#         print('bus')
#         continue
#     print(x)


# p1 = input('Enter R(rock) or P(paper) or S(scissor)')
# p2 = input('Enter R(rock) or P(paper) or S(scissor)')
#
# if (p1=='R' and p2=='P'):
#     print('p2 wins')
# elif (p1=='P' and p2=='R'):
#     print('p1 wins')
# else:
#     pass


# def Elakkiya(): #function with no argument and no return value
#     print('My name is Elakkiya')
#
# Elakkiya()

# def svr(): #fn with no argument and a return value
#     print('Python')
#     a = 'dskbs'
#     return a
#
# name = svr()
# print(name)
#
# def functionArgument(a): #with argument & no return
#     print(a)
#
# functionArgument(123)
# functionArgument(456)
#
# def fnReturn(x): #fn with argument and with return value
#     return x
#
# abc = fnReturn(123)
# print(abc)

# a = 5
# a = input()
# list_of_items = [1,2,3,4,5]

# list_of_items = [] #[5,7,9] #step 1
# user_wish = input('Do you want to add items to the list y/n')
# while (user_wish == 'y'):
#     a = input('Enter the item')
#     list_of_items.append(a)
#     user_wish=input('Do you want to add more? y/n')
# print(list_of_items)

# list_of_items = []
# no_of_items = int(input('How many items do you wish to add?'))
# for i in range(no_of_items):
#     # print(i)
#     a = input('Enter the item')
#     list_of_items.append(a)
# print(list_of_items)

# Word counter
# list_of_words = input('Enter the data').split()
# no_of_words = len(list_of_words)
# print(f"you have {no_of_words} words in the given data")

# # Even and odd list
# list_of_numbers = input('enter the numbers').split()
# even_list = []
# odd_list = []
#
# for each in list_of_numbers:
#     if int(each) % 2 == 0:
#         even_list.append(each)
#     else:
#         odd_list.append(each)
# print('Even List is ',even_list)
# print('Odd list is ',odd_list)

# Prime no checking program
# def checkPrime(number):
#     for i in range(2,number):
#         if (number % i == 0):
#             return f"{number} is not a prime number"
#     return f"{number} is a prime number"
#
# num = int(input('Enter a number to check: '))
# print(checkPrime(num))


# # Todo List Program
#
# list_of_tasks = [] #creating a container to store tasks
#
# print('Welcome to my to-do list project') #welcome message
#
# while(True): #to run the app in a loop infinitely
#     #getting user option on the feature
#     option = int(input('\n1.Add a task\noption: '))
#
#     if (option == 1): #checking user's request
#         task = input('Name of the task to be added: ') #get task details from user
#         if task not in list_of_tasks: #check if task is dupicate or not
#             list_of_tasks.append(task) #adding the task to list if task is not duplicate
#             print('task added successfully') #success message if task is not duplicate
#         else: #if task is duplicate
#             print('task not added as it is a duplicate') #failure message

# File operations:

f = open('elakiya.txt','w')
f.write('Elakiya is an excellent student')
f.close()

f = open('elakiya.txt','a')
f.write('Elakiya is studying Python')
f.close()

f = open('elakiya.txt')
print(f.read())


