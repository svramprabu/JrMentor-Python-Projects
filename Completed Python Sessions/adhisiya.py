# saved_password = 'adhisiya123'
# user_password = input('Enter the password')
# if (saved_password == user_password):
#     print('Success')
# else:
#     print('Fail')

# list_of_items = ['car','bike','train','ship']
# print(list_of_items)
# for i in list_of_items:
#     print(i)

# i = 1
# while (i<10):
#     print(i)
#     i+=1 # i = i+1

# saved_password = 'adhisiya123'
# user_password = ''
# wrong_attempts=0
# while (saved_password != user_password):
#     user_password = input('enter the password') #step 1
#     if (saved_password == user_password): #step 2
#         print('Success') #step 3
#     else:
#         print('retry') #step 3
#         wrong_attempts+=1 #step 3
#     if (wrong_attempts==3): #step 4
#         break #step 5

# i = 1
# while (i<10):
#     i+=1 # i = i+1 #step 1
#     if (i==4): #step 2
#         pass
#         # break
#         # continue
#     print(i) #step 3

# Completed Python Sessions function with no argument and a return value

# def subraction():
#     a = 30
#     b = 10
#     sub = a - b
#     return sub
#
# print(subraction())

# Completed Python Sessions function with argument but no return value

# def multiplication(a,b):
#     mul = a*b
#     print(mul)
#
# multiplication(2,3)

# Completed Python Sessions function with arguments and return value

# def division(a,b):
#     div = a/b
#     return div
#
# print(division(10,2))

# Arguments
#
# pass by value
# adhisiya(10,20)
#
# pass by reference
# a = 10
# b = 20
# adhisiya(a,b)

#rock paper scissor
# p1 = input('Enter Rock(r) or paper(p) or scissor(s)')
# p2 = input('Enter Rock(r) or paper(p) or scissor(s)')
#
# if (p1=='r' and p2=='p'):
#     print('player2 wins')
# elif (p1=='p' and p2=='r'):
#     print('player1 wins')
# elif (p1=='r' and p2=='s'):
#     print('player1 wins')
# elif (p1=='s' and p2=='r'):
#     print("player2 wins")
# elif (p1=='s' and p2=='p'):
#     print("player1 wins")
# elif (p1=='p' and p2=='s'):
#     print("player2 wins")
# elif (p1=='r' and p2=='r'):
#     print("draw")
# elif (p1=='s' and p2=='s'):
#     print("draw")
# elif (p1=='p' and p2=='p'):
#     print("draw")
# else:
#     print('Invalid input')

#word counter
# essay = input('Paste the data: ').split()
# number_of_words = len(essay)
# print(number_of_words,'words are there in the given essay.')

#student report
# student_name = input('enter the student name: ')
# eng_mark = int(input('Enter the english marks: '))
# tam_mark = int(input('Enter the tamil marks: '))
# math_mark = int(input('Enter the maths marks: '))
# total = eng_mark + tam_mark + math_mark
# print()
# print('Welcome',student_name)
# print('you have scored a total marks of',total)

# #prime number checking
# def checkPrime(number):
#     for i in range(2,number):
#         if (number % i == 0):
#             return number,"is not prime"
#     return number,"is prime"
#
# num = int(input('Enter a number: '))
# print(checkPrime(num))

# #list of students
# number_of_students = int(input('Enter the number of students: '))
# students = []
# for i in range(number_of_students):
#     student_name = input('Enter the name: ')
#     students.append(student_name)
# print(students)

a = 45 #global variable
print(a)
def func():
    # global b
    b = 66 #local variable

func()
print(b)