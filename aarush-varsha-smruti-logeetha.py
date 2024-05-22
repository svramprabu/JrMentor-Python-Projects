# # Tuple

# to store multiple data
# can store duplicate items

# differences
# 1. List -> [] Tuple -> ()
# 2. List is Mutable while tuple is immutable

# eg_list=[34,35,36,37]
# print(eg_list)
# eg_list[2]=45
# print(eg_list)

# eg_tuple=(34,35,36,37)
# print(eg_tuple)
# # eg_tuple[2]=45
# eg_tuple = (34,35,45,37)

# empty_tuple = ()
# mixed_tuple = (1,'Hi',4.45)

# Attributes in list

# eg_list = [1,2,3,4,5]
# print(len(eg_list)) #to find the length of the list
#
# eg_list.append(6) #to add a new item to the list
# print(eg_list)
#
# eg_list.remove(5) #to remove a value from list
# print(eg_list)
#
# print(min(eg_list)) #to find the minimum value in a list
# print(max(eg_list)) #to find the maximum value in a list

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

# Assignment operators
a = 10
# +=
a += 10 # a = a+10
# print(a)

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

# 0101011
# 0010101
# print(5 & 3)

a=input('a=')
b=input('b=')
if (a>b):
    print('a is greater than b')
    print('if statement')
else:
    print('a is not greater than b')
    print('else statement')