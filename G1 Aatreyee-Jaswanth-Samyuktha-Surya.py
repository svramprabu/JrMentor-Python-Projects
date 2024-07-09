# print("Hi and welcome to Hackerkid program")

# var_123 = 12345
# print(var_123)

# a = 123
# print(a)
# print(type(a))
#
# b = 123.45
# print(b)
# print((type(b)))

# c = "Hi and Welcome to Hackerkid Day 3!!!"
# print(c)
# print(type(c))
#
# True,False #Boolean
# print(type(True))
# print(type(False))

# declare three variables name,age,weight and store the data and print their datatypes
# name = 'Ram'
# print(name)
# print(type(name))
#
# age = 30
# print(age)
# print(type(age))
#
# weight = 75.5
# print(weight)
# print(type(weight))

# example_list = [1,2,3,4,5] #integer list
# print(example_list)
# ex_list = ['jaswanth','aatreyee','samyuktha','surya','mukundan'] #strign only list
# print(ex_list)
# my_list = [123,456,67.89,'Python'] #mixed list
# print(my_list)
# empty_list = []
# print(empty_list)
# # Nested list
# nested_list = [123,[1,2,3]]
# print(nested_list)

# s = 'Python'
# print(s)
# print(s[0])
# print(s[2])
#
# print(s[-1])
# print(s[-3])

# declare a variable and store the alphabets as a string and print the
# vowels using string access

# s = 'abcdefghijklmnopqrstuvwxyz'
# # vowels -> a e i o u
# print(s[0]) #a
# print(s[4])
# print(s[8])
# print(s[-12])
# print(s[-6])

# my_list = ['Aatrayee','Mukundan','Jaswanth','Surya','Samyuktha']
# print(my_list)
# print(my_list[3])
# print(my_list[-1])
# print(my_list[5]) #index error
# print(my_list[3.0]) #type error

# my_list = [1,2,3,4,5]
# my_tuple = (1,2,3,4,5)

# empty_tuple
# integer_tuple
# mixed_tuple
# nested_tuple

# list is mutable
# my_list = ['Aatrayee','Mukundan','Jaswanth','Surya','Samyuktha']
# print(my_list) #before mutation
# my_list[3] = 'surya vishwanand'
# print(my_list) #after mutation

# my_tuple = ('python','java')
# my_tuple[1]='C++'

# []
# ()

# my_list = ['Aatrayee','Mukundan','Jaswanth','Surya','Samyuktha']
# my_list[2]

# empty_dict = {}
# print(empty_dict)
#
# my_dict = {1:'Apple',2:'Orange'} #integer keys
# print(my_dict)
#
# my_dict = {'Name':'Python','Class':'Hackerkid'} #string keys
# print(my_dict)
#
# my_dict = {1:'Python','Name':'Pycharm'} #mixed keys
# print(my_dict)
#
# my_dict = {1:'Python','Name':'Pycharm'}
# print(my_dict['Name']) #description

# Typecasting
# a = 10
# b = '15'
# b = int(b) #typecasting to integer
# add = a+b
# print(add)

# name = input('What is your name')
# print(name)
# print(type(name))
#
# age = int(input('What is ur age '))
# print(age)
# print(type(age))
#
# weight = float(input('What is ur weight '))
# print(weight)
# print(type(weight))

# a = 10
# b = 15
# c = 20
# print(a,b,c)
# print(a,b,c,sep='--->')
# print(a,sep='->')
#
# print(a,end='\n')
# print(a,end='$$$')
# print(b)
#
# print(a,b,c,sep='--->',end='$$$')

# x = 11
# y = 2
# print('x+y=',x + y) #addition
# a = 'Python'
# b = 'Programming'
# print('a+b=',a + b) #concatenation
#
# print('x-y=',x - y) #subtraction
# print('x*y=',x * y) #multiplication
#
# print('x/y=',x / y) #division
# print('x%y=',x % y) #remainder
# print('x//y=',x // y) #modulus quotient
#
# print('x**y=',x**y) #power x*x*x 11x11

# Take input from user collecting marks in different subject
# 5 subjects
# output total marks

# E = int(input('English: '))
# M = int(input('Maths: '))
# S = int(input('Science: '))
# Total = E+M+S
# print('Total marks in the exam is',Total)

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

# find the age from birth year
# take input from the user asking for his/her birth year
#     calculate the age using that and print a statement
# that says "As your were born in 1994 your age is 30"

# birth_year = int(input('Enter your birth year: '))
# age = 2024 - birth_year
# print(f"As you were born in {birth_year} your age is {age}")


# age = int(input('Enter your age: '))
# print(age>18,'True mean ELigible to vote',sep='--->')

# a = 10
# print(a)
# a += 10 #a+10 then 20 -> a=20
# print(a)

# Identity Operators
# (is) ==
# (is not) !=
# a = 10
# b = 20
# print(a is b)
# print(a  is not b)

# Logical operators

# and (Multiplication)
# True 1
# False 0

# print(True and True) #(1*1) True
# print(True and False) #False
# print(False and True) #False
# print(False and False) #False

# print(5>3 and 5>4) use case of logical operator

# or (addition)
# print(True or True) #(1+1) True
# print(True or False) #True
# print(False or True) #True
# print(False or False) #False

# not
# print(not True) #False
# print(not False) #True

# Bitwise Operator
# & | ~ ^
# print(2 & 3) #bitwise and

# Membership Operators
# in
# not in

# x in y
# x not in y

# Concatenation:
# Python program to generate full name given two variable
# first_name (has the first name stored in it) and
# last_name (has last name stored in it)

# first_name = "Ramprabu"
# last_name = "SV"
# full_name = first_name + last_name
# print(full_name)

# Python program to find the number of toys x has
# if he/she own 2 aeroplanes, 5 helicopters and 11 trains.
# aeroplanes = 2
# helicopters = 5
# trains = 11
# toys = aeroplanes+helicopters+trains
# print(f'The number of toys are {toys}')

# Python program to find the cost
# if x plans to buy 8 apples at the price of 17 each

# apples = 8
# price_of_apple = 17
# cost_of_apples = apples * price_of_apple
# print(f'Cost of the 8 apple at 17 each is {cost_of_apples}')

# Python program to find how many litres of petrol can be
# filled in 4 bikes given we have only 14 litres of petrol.

# petrol = 14
# bikes = 4
# petrol_in_bike = petrol / bikes
# print(f"Petrol in each bike is {petrol_in_bike} litres")

# Python program to find the number of persons that can occupy in
# each cup of a giant wheel with 5 cups and 12 persons.
# Also, find the number of persons who don’t get to ride in it.

# no_of_cups = 5
# no_of_persons = 12
# no_in_each_cup = no_of_persons // no_of_cups
# person_not_ride = no_of_persons % no_of_cups
# print(f'We can have {no_in_each_cup} persons in each cup and {person_not_ride} persons '
#       f'didnt get chance to ride')

# if condition:
#       statement 1
#       staement 2
#       statement 3
# statement

# if (5 > 3):
#       print('Five')
#       print('Greater than')
#       print('Three')

# age = int(input('Enter your age: '))
# if (age > 18):
#       print('You are Eligible to vote')

# if Condition:
#       Statement
# else:
#       Statement

# if (5>10):
#       print('Yes')
# else:
#       print('No')

# height = int(input('Enter height: '))
# if (height > 150):
#     print('Enjoy the ride')
# else:
#     print('Grow up please')

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


# a = int(input('a='))
# b = int(input('b='))
# if (a > b):
#     print('a>b')
# elif (a < b):
#     print('a<b')
# else:
#     print('a = b')

# get age
# Kg 5
# Primary 10
# Secondary 15
# Higher secondary 18

# age = int(input('Enter the age: '))
# if age < 5:
#     print('KG')
# elif age < 10:
#     print('Primary')
# elif age < 15:
#     print('Secondary')
# elif age < 18:
#     print('Higher secondary')
# else:
#     print('Does not belong in school')

# Rock Paper Scissor
# rps.py
# 3 ^ 2 = 9
# r p
# p r
# r s
# s r
# s p
# p s
# s s
# r r
# p p

# p1 = input('Choose Rock(r) or Paper(p) or Scissors(s): ').lower()[0]
# p2 = input('Choose Rock(r) or Paper(p) or Scissors(s): ').lower()[0]
#
# if (p1 == 'r' and p2 == 'p'):
#     print('player 2 wins')
# elif (p1 == 'p' and p2 == 'r'):
#     print('player 1 wins')
# elif (p1 == 'p' and p2 == 's'):
#     print('player 2 wins')
# elif (p1 == 's' and p2 == 'p'):
#     print('player 1 wins')
# elif (p1 == 's' and p2 == 'r'):
#     print('player 2 wins')
# elif (p1 == 'r' and p2 == 's'):
#     print('player 1 wins')
# elif (p1 == p2):
#     print('it is a tie')
# else:
#     print('invalid input')


# days_of_week = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
#
# user_input = input('Enter a day of the week: ').lower() #MONDAY -> monday
# if (user_input == days_of_week[0]): #user_input == 'monday'
#     print('Ohh I hate mondays')
# elif (user_input == days_of_week[4]):
#     print('Yeaaaa Weekend begins today')
# elif (user_input == days_of_week[5] or user_input == days_of_week[6] ):
#     print('Fun dayyssss')
# elif (user_input in days_of_week):
#     print('Yet another day of the week')
# else:
#     print('invalid input')


# for i in sequence:
#     statement

# my_list = ['surya','aatrayee','jaswanth','samyuktha','mukunthan']
# for each_name in my_list:
#     print(each_name)

# Acronym Generator program
# United States -> US
# United Kingdom -> UK
# Indian Space Research Organization -> ISRO

# user_input = input('Enter: ').split()
# ans = ''
# for each_word in user_input:
#     ans += each_word[0]
# print(ans)

# paragraph = input('Paste here: ')
# words = paragraph.split()
# no_of_words = 0
# for each_word in words:
#     no_of_words += 1
# print(f'Number of words in the paragraph is {no_of_words}')

# name = 'Ramprabu'
# for i in name:
#     print(i)

# s = input('Enter a string: ')
# letter = input('Enter a letter: ')
# answer = 0
# for each_letter in s:
#     if (each_letter.lower() == letter):
#         answer += 1
# print(f"The letter {letter} has occured {answer} times in '{s}'")

# s = input('Enter a string: ') #Ramprabu -> rampbu
# ans = ''
# for each_letter in s:
#     if (each_letter.lower() not in ans):
#         ans += each_letter.lower()
# print(f'Answer string in {ans}')

# for i in range(100): #[0,1,2,3,4]
#     print(i)
#
# for i in range(5,10):
#     print(i)

# start = int(input('enter a starting range: '))
# end = int(input('Enter an ending range: '))
# for i in range(start,end):
#     print(i)

# 1 x 2 = 2
# 2 x 2 = 4
# 3 x 2 = 6
# ...
table_no = int(input('Enter table no: '))
for i in range(1,11):
    print(f"{i} X {table_no} = {i * table_no}")