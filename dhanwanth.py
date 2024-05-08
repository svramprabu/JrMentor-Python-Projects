# name = 'Dhanwanth'
# print(name)
# print(name[4])
# print(name[7])
#
# alphabets = 'abcdef....'
# # aeiou
# print(alphabets[0])

# x = 10 #int
# y = '15' #string
# y = int(y) #type casting
# addition = x+y
# print(addition)
#
# a = 1 #int()
# b = 1.3 #float()
# c = '2.6'

# a = input('Enter your name')
# print(a)

# age = input('Enter your age')
# age = int(input('Enter your age'))

a = 10
b = 5

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)

# a = 10
# b = 15
# print(a & b) #bitwise and
# print(a | b) #bitwise or

# list_of_things = ['book','note','pen','pencil']
# print('guide' in list_of_things)
# print('guide' not in list_of_things)

# is ==

# if condition:
#     statement

# Syntax:

# if condition:
#     statement
# elif condition:
#     statement
# elif condition:
#     statement
# elif condition:
#     statement
# else:
#     statement

# number = int(input('Enter a no'))
# if number > 10:
#     print('number is greater than 10')
# elif number < 10:
#     print('number is smaller than 10')
# else:
#     print('number is 10')

# saved_password = 'Dhanwanth'
# user_password = input('Enter the right password: ')
#
# if (saved_password == user_password):
#     print('Success')
# else:
#     print('Failure')

# lang_list = ['python','java','c++']
# print(lang_list)
# for i in lang_list:
#     print(i)

# for i in range(5):
#     print(i)
#     print('Dhanwanth')

# Print a multiplication table
# table = int(input('Enter table no: '))
# for i in range(1, 11):
#     print(i, 'x', table, '=', i * table)

# a = int(input('a='))
# b = int(input('b='))
# for i in range(a,b):
#     print(i)



# While loop
# i = 1
# while (i<10):
#     print(i)
#     # i = i+1
#     i += 1

# cycle 1: i=1 -> 1<10 -> True -> print(1) -> i = i+1 -> i = 2
# cycle 2: i=2 -> 2<10 -> True -> print(2) -> i = i+1 -> i = 3

# Python program to count the number digits in a number

n = int(input('Number = ')) #12345
ans = 0
while (n>0):
    n=n // 10 #modulus 1234 123 12 1 0
    ans = ans + 1
print('Total number of digits: ',ans)
