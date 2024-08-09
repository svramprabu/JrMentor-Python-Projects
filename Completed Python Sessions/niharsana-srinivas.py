# print('Hi and welcome to HackerKid')
# name = 'srinivas'
# #       0123
# print(name)
# print(name[3])
#
# a = 'programming'
# #    012345
# print(a)
# print(a[5])
#
# x = 'jkdsfbDBjsbvskdvbsbv'
# print(x[-1])
#
# test = 'Hi my name is Srinivas'
# print(test[-1])  # s
#
# # Length of the string
# # len(variable_name)
#
# alphabets = 'abcdefghijklmnopqrstuvwxyz'
# print(len(alphabets))

# x = 'Ramprabu'
# print(x)
# y = input('y=')
# print(y)

# name = input('What is your name? : ')
# print(name)
# age = int(input('What is your age? : '))
# print(age)
# weight = float(input('What is your weight? : '))
# print(weight)
#
# print(name,age,weight)
# print()
# print(name,age,weight,sep='->')

# x = 11
# y = 2
# print('x+y=',x + y)
# a = 'Completed Python Sessions'
# b = 'Programming'
# print('a+b=',a + b) #concatenation
#
# print('x-y=',x - y)
# print('x*y=',x * y)
# print('x/y=',x / y)
# print('x%y=',x % y) #remainder
# print('x//y=',x // y) #quotient
# print('x**y=',x ** y)

# eng = int(input('Englis: '))
# tam = int(input('Tamil: '))
# math = int(input('Maths: '))
#
# Total = eng+tam+math
# print(f'You scored a total of {Total} marks in the exam')

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


# a = 15
# print('basic assignment operation',a)
# a += 5 # a+5,a=result -> a=a+5
# print('complex assignment operation',a)
#
# b = 25
# b -= 8
# print(b)

# Logical operators

# and (Multiplication)
# True 1
# False 0

# print(True and True) #(1*1) True
# print(True and False) #False
# print(False and True) #False
# print(False and False) #False
#
# print(5>3 and 5>4) #example use case of logical operator
#
# # or (addition)
# print(True or True) #(1+1) True
# print(True or False) #True
# print(False or True) #True
# print(False or False) #False
#
# # not
# print(not True) #False
# print(not False) #True

# if (5 > 3):
#     print('Five')
#     print('is greater than')
#     print('Three')

# a = int(input('a='))
# b = int(input('b='))
# if (a<b):
#     print('a is less than b')
# else:
#     print('a is greater than b')

# a = int(input('a='))
# b = int(input('b='))
# if (a<b):
#     print('a is less than b')
# elif (a>b):
#     print('a is greater than b')
# else:
#     print('a is equal to b')

# age = int(input('Enter the student age: '))
#
# if (age < 5):
#     print('KG')
# elif (age < 10):
#     print('Primary')
# elif (age < 16):
#     print('Secondary')
# elif (age < 18):
#     print('Higher Secondary')
# else:
#     print('Does not belong in school')

# Acronym Generator
# United states US
user_input = input('Enter the expanded form: ').split()
acronym = ''
for each_word in user_input:
    acronym += each_word[0]
print(f'The acronym is {acronym}')

# paragraph = input('Enter paragraph: ') #getting input
# words = paragraph.split() #splitting word by word
# count = 0
# for word in words:
#     count += 1 #count+1 -> count = new value
# print('Number of words in the paragraph are',count)