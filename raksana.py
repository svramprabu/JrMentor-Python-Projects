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
p1 = input('Enter Rock(r) / paper(p) / scissor(s)')
p2 = input('Enter Rock(r) / paper(p) / scissor(s)')

#part 2 condition checking
if (p1 == 'r' and p2 == 'p'):
    print('player 2 wins')
elif (p1 == 'p' and p2 == 'r'):
    print('player 1 wins')
elif (p1 == 'r' and p2 == 's'):
    print('player 1 wins')
elif (p1 == 's' and p2 == 'r'):
    print('player 2 wins')




