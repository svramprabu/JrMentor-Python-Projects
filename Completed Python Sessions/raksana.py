# # # 1. declare a variable with all alphabets
# # a = 'abcd....'
# #
# # # 2. print the variable
# # # print(a)
# #
# # # 3. print all vowels (a,e,i,o,u)
# # print(a[0])
# # # print(a[4]) # this line will print e
#
#
# # print(a,b,3,4,5,sep='@',end='&&&&&')
# # print(a,end='>>>>')
#
# # declare two variables
# # get input from user
# # 1. name
# # 2. age - int
# # print with ---- as a seperator and
# # use ******** as end argument
#
# # user_name =input("What's ur name?")
# # user_age = int(input("What's your age?"))
# # print(user_name,user_age,sep='----')
#
# # import ram
#
# # a = int(input('Enter a'))
# # b = int(input('Enter b'))
# # print(a+b)
# # print(a-b)
# # print(a*b)
# # print(a/b)
# # print(a%b)
# # print(a**b) #2**4 2X2X2X2
# # print(a<=b) #a>b a==b
#
# # a = 'abcdefg'
# # print(a)
# # print(a[0])
# # print(type(a))
#
# # comments
# # 1. skip ctrl+/
# # 2. comment or explanation #give your comment
#
# # Type conversion
# # 1. Implicit
# # 2. Explicit or type casting
# # a
# # int(a)
# # float(a)
# # str(a)
# # a=5
# # b='5'
# # c=int(b)
# # print(a+c)
#
# # a = 5
# # x = 67.8
# # d = 'jdfbn'
#
# # b = input('Enter your name') #default str
# #
# # k = input('Enter a no')
# # # method 1 :
# # k=int(k)
# # # method 2:
# # k = int(input('enter a no'))
#
# # print(a,x) #output
# # print(a)
# # print(x)
#
# # print(5+10)
#
# # a = int(input('Enter a no'))
# # b = int(input('Enter a no'))
# # print(a+b) #addition
# # print(a-b) #subtraction
# # print(a*b) #multiplication
# # print(a/b) #division
# # print(a%b) #remainder
# # print(a**b) #power or exponentiation
#
# # Comparison operators
# a = int(input('a = '))
# b = int(input('b = '))
#
# # Greater than (>)
# print(a,'>',b)
# print(a > b)
#
# # Lesser than (<)
# print(a,'<',b)
# print(a < b)
#
# #value equals (==)
# print(a,'==',b)
# print(a == b)
#
# #value not equals (!=)
# print(a,'!=',b)
# print(a != b)
#
# #greater than or equal to (>=)
# print(a,'>=',b)
# print(a >= b)
#
# #lessthan or equal to (<=)
# print(a,'<=',b)
# print(a <= b)
#
# # Tuple:
# # - Tuple is similar to a list except it is immutable (can not edit the individual items)


# Student Report
# student_name = input('Enter student name: ')
# eng_marks = int(input('English marks: '))
# tam_marks = int(input('Tamil marks: '))
# math_marks = int(input('Maths marks: '))
# sci_marks = int(input('Science marks: '))
# soc_marks = int(input('Social marks: '))
#
# total_marks = eng_marks + tam_marks + math_marks + sci_marks + soc_marks
# average_marks = total_marks / 5
#
# print()
# print('Hi',student_name)
# print('English marks: ',eng_marks)
# print('Tamil marks: ',tam_marks)
# print('Maths marks',math_marks)
# print('Science marks: ',sci_marks)
# print('Social marks: ',soc_marks)
# print('You have a total marks of',total_marks,'with an average marks of',average_marks)



#Adding items to a list

# student_details = []
# #collecting data from the user
# student_name = input('Enter student name: ')
# math_marks = int(input('Maths marks: '))
# sci_marks = int(input('Science marks: '))
# soc_marks = int(input('Social marks: '))
# #calculation
# total_marks = math_marks + sci_marks + soc_marks
# average_marks = total_marks / 5
# #appending items to the list
# student_details.append(student_name)
# student_details.append(total_marks)
# student_details.append(average_marks)
#
# print(student_details)
#
# age = int(input('Enter the age: '))
# if (age > 15):
#     print('Higher secondary student')
# elif (age > 10):
#     print('High school student')
# elif (age > 5):
#     print('Primary school stududent')
# else:
#     print('Kindergarten')

# Even or odd in a list and creating a new list
# [1,2,3,4,5]
# [1,3,5]
# [2,4]

# list_of_nos = [1,2,3,4,5,6,7,8]
# number = int(input('enter a number: '))
# if (number % 2 == 0):
#     print(f'{number} is Even number')
# else:
#     print(f'{number} is Odd number')


# Rock paper scissor
# part 1 getting input from players
# p1 = input('Enter Rock(r) / paper(p) / scissor(s)')
# p2 = input('Enter Rock(r) / paper(p) / scissor(s)')
#
# #part 2 condition checking
# if (p1 == 'r' and p2 == 'p'):
#     print('player 2 wins')
# elif (p1 == 'p' and p2 == 'r'):
#     print('player 1 wins')
# elif (p1 == 'r' and p2 == 's'):
#     print('player 1 wins')
# elif (p1 == 's' and p2 == 'r'):
#     print('player 2 wins')



# Password checker program
# stored_password = 'raks123'
# user_password = input("Enter the password: ")
#
# if (user_password == stored_password):
#     print('Success')
# else:
#     print('Failure')

# list_of_toys = ['doll', 'car', 'bike']
# for i in list_of_toys:
#     print(i)
#
# for i in range(10):  # -> [0,1,2,3,4]
#     print('Raksana')
#     print(i)

# import random
# options = ['r','p','s']
# user_play=int(input('1.play 2.exit'))
# while(user_play == 1):
#     computer_option = random.choice(options)
#     player_option = input('Enter Rock (r) or Paper (p) or Scissor (s): ')
#
#     if (computer_option == 'p' and player_option == 'r'):
#         print('Computer won')
#     elif (computer_option =='r' and player_option == 'p'):
#         print('You won')
    # r s
    # s r
    # p s
    # s p

# i = 1
# while (i < 10):
#     if (i == 4):
#         break
#     print(i)
#     i+=1

# Password checker program
# stored_password = 'raks123'
# while(True):
#     user_password = input("Enter the password: ")
#
#     if (user_password == stored_password):
#         print('Success')
#         break
#     else:
#         print('Failure')

# w = 0
# stored_password = 'raks123'
# while(True):
#     user_password = input("Enter the password: ")
#
#     if (user_password == stored_password):
#         print('Success')
#         break
#     else:
#         w += 1
#         print(f'Failure with {w} wrong attempts')
#         if (w == 3):
#             print("You have exceeded the maximum attempts")
#             break

# i = 0
# while (i < 10):
#     i += 1
#     if (i == 6):
#         continue
#     print(i)
#
# saved_password = 'Raksana123'
# count=0
# while(True):
#     user_password = input('Password: ')
#     if (user_password == saved_password):
#         print('Success')
#         break
#     elif ('Raksana' in user_password):
#         pass
#         # print('Your password is semi correct')
#         # continue
#     else:
#         count+=1
#         print('Try again')
#     print(f"You have used {count} attempts")


# User Defined Function types
# Type 1 no argument and no return value
# def func1():
#     print(5+3)

# func1()

# Type 2 no argument but a return value
# def func2():
#     return 5+5

# a = func2()
# print(a)

# print(func2())

# Type 3 with argument but no return value
# a=15
# def func3(a,b):
#     print(a,b)
#
# func3(15,20)

# Type 4 with both argument and return value
# def func4(a):
#     return (a)
#
# print(func4(25))

# Calculator program using functions
# def add(): #type 1 no argument & no return value
#     a = int(input('a='))
#     b = int(input('b='))
#     print(f'{a}+{b}={a+b}')
#
# def sub(): #type 2 no argument with return value
#     a = int(input('a='))
#     b = int(input('b='))
#     return f"{a}-{b}={a - b}"
#
# def mul(a,b): #type 3 with argument and no return
#     print(f"{a}x{b}={a*b}")
#
# def div(a,b): #type 4 with argument and return value
#     return f"{a}/{b}={a/b}"

# print('Welcome to my calculator app')
# while(True):
#     user_option = int(input("1.add\n2.sub\n3.mul\n4.div\n5.exit\nEnter your desired option: "))
#     if (user_option == 1):
#         print('You chose addition function')
#         add()
#     elif (user_option == 2):
#         print("You chose Subtraction function")
#         print(sub())
#     elif (user_option == 3):
#         print("You chose Multiplication function")
#         a = int(input('a='))
#         b = int(input('b='))
#         mul(a,b)
#     elif(user_option == 4):
#         print("You chose Division function")
#         a = int(input('a='))
#         b = int(input('b='))
#         print(div(a,b))
#     elif(user_option == 5):
#         print('Thank you for using my calculator ')
#         break
#     else:
#         print("enter the correct option")

# def rps(p1,p2):
#     if (p1 == 'r' and p2=='p'):
#         print('player 2 wins')
#     elif (p1 == 'p' and p2=='r'):
#         print('player 1 wins')
#     elif (p1 == 'p' and p2=='s'):
#         print('player 2 wins')
#     elif (p1 == 's' and p2=='p'):
#         print('player 1 wins')
#     elif (p1 == 's' and p2=='r'):
#         print('player 2 wins')
#     elif (p1 == 'r' and p2=='s'):
#         print('player 1 wins')
#     elif (p1 == p2): #p p r r s s
#         print('It is a Tie')
#     else:
#         print('Invalid Input')
#
# print('Welcome to Rock paper scissors game\n')
# game_mode = int(input('1.Single player \n2.Double player \nEnter game mode '))
# if (game_mode == 1):
#     import random
#     Human_user = input('Enter Rock(r) or Paper(p) or Scissors(s): ').lower()
#     Computer_user = random.choice(['r','p','s'])
#     print(f"Computer chose {Computer_user}")
#     rps(Human_user,Computer_user)
# elif (game_mode == 2):
#     player_1 = input('Enter Rock(r) or Paper(p) or Scissors(s): ').lower()
#     player_2 = input('Enter Rock(r) or Paper(p) or Scissors(s): ').lower()
#     rps(player_1,player_2)

# from new_package import module1
# module1.func()

# import random
# chosen_number = random.randint(1,100)
# print('I have a number in mind can you find it????')
# while(True):
#     user_number = int(input('Find the number: '))
#     if user_number > chosen_number:
#         print('Enter a smaller number')
#     elif user_number < chosen_number:
#         print('Enter a bigger number')
#     else:
#         print('You found the number chosen by computer')
#         break
# print('Thank you for playing with me')

f = open('raksana.txt','w')
f.write('Hi, my name is Raksana from Completed Python Sessions class')
f.close()

f = open('raksana.txt','a')
f.write(' I am appending to the text file')
f.close()

f = open('raksana.txt')
print(f.read())

