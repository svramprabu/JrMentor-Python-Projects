# # a = 23
# # b = 39
# # print(a&b)
# #
# # def room1():
# #     d = 1
# #     print(d)
#
#
# # if (5>2):
# #     print('5 is greater than 2')
#
# # saved_password='vedansh123'
# # user_password = input('Please enter the password')
# # if (saved_password == user_password):
# #     print('Success')
# # elif ('vedansh' in user_password):
# #     print('Semi correct')
# # else:
# #     print('Wrong password')
#
# # list_of_names = ['vedansh','bansal','vedanshbansal']
# # print(list_of_names)
# # for name in list_of_names:
# #     print(name)
#
# # for i in range(10):
# #     print('Apple')
# #     print(i)
#
# # i = 1
# # while (i<10):
# #     print(i)
# #     i+=1 #i=i+1
#
# # saved_password = 'vedansh123'
# # user_password = ''
# # while(saved_password != user_password):
# #     user_password = input('Enter the password')
# #     if (user_password == saved_password):
# #         print('Success')
# #     else:
# #         print('Retry')
#
# # i = 1
# # while (i<10):
# #     print(i)
# #     if (i == 4):
# #         # statement
# #         pass
# #     i+=1
#
# # while(True):
# #     if egg is bad
# #         continue
# #     paint the egg
#
# # step 1 input of no
# # for loop
# # for i in range(1,11):
#     # print(i,'x','input no','=','i * input no')
# # user = int(input('Enter a no '))
# # for i in range(1,11):
# #     print(f'{user}x{i}={user*i}')
#
# # def addition(a,b):
# #     # a = 10
# #     # b = 15
# #     sum = a + b
# #     print('after calling',sum)
# # a=10
# # b=20
# # addition(a,b)
# # print(b)
# # print(addition())
#
#
#
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b
#
# print("""Welcome to my calculator
# Choose you desired option
# 1. addition
# 2. subtraction
# 3. multiplication
# 4. division""")
#
# user_option = int(input("Enter your option: "))
# if (user_option == 1):
#     a = int(input('a = '))
#     b = int(input('b = '))
#     print(f'Additon of {a} & {b} is ',add(a,b))
#
# elif (user_option == 2):
#     a = int(input('a = '))
#     b = int(input('b = '))
#     print(f'Subtraction of {a} & {b} is ', sub(a, b))

# Acronym generator
# input Indian Space Research Organisation
# output ISRO

# user_data = input('enter the data').split()
# print(user_data)
# ans=''
# for each in user_data:
#     ans=ans+each[0]

# my_list = [1,2,3,4,5]
# my_tuple = (1,2,3,4,5)
# print(my_list)
# print(my_tuple)
# my_list[2]='two'
# print(my_list)
# # my_tuple[2]='three'
# my_tuple = (1,2,'three',4,5)
# print(my_tuple)


# n_list = ['vedansh',[49.4,50,49]]
#
# my_dict = {1:'apple',2:'orange'}
# my_dict = {'English':49.4,'Maths':50,'Science':49}
# print(my_dict)
#
# # [[name,marks],[],[]]
# [['vedansh',{'eng':50,}],[],[]]

# from vedansh_package import module1
# module1.mod_function()

# Dice simulator
# import random
# while(True):
#     user_choice=int(input('\n1. Roll\n2. Exit \nChoose an option: '))
#     if (user_choice == 1):
#         chosen_number = random.randint(1,6)
#         print(f"You got {chosen_number} after rolling the dice")
#     elif (user_choice == 2):
#         print('Thank yoy for playing')
#         break
#     else:
#         print('Sorry wrong option')
#         continue


# import random
# x= 'abcdefg'
# print(''.join(random.sample(x,3)))

# f = open('vedansh.txt','w')
# f.write('Vedansh is a talented student')
#
# f = open('vedansh.txt')
# print(f.read())
#
# f.close()

# class Parent:
#     def __init__(self,parentname):
#         print('Hii from parent class')
#         self.parentname = parentname
#
# class Child1(Parent):
#     def __init__(self,parentname):
#         print('Hii from child1')
#         Parent.__init__(self,parentname)
# a = Child1('Abba')
# print(a.parentname)
# a.func1()

# import random
# options = ['r','p','s']
# com=random.choice(options)
# print(com)
# p =
# while(True):

# class bird:
#     def flight(self):
#         print('Birds can fly')
#
# class sparrow(bird):
#     pass
#
# class ostritch(bird):
#     def flight(self):
#         print('Ostritch cannot fly')
#
# a = sparrow()
# a.flight()
# b = ostritch()
# b.flight()

# Why class?
# class int
# print(type(123))

# class
# list = [1,2,3,4,5,6]
# contiguous memory location
# append

# Linked List
# space - data
# space2 - address to the next data
# flow always starts from first element
# no reverse flow

# class LinkedList:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#     def next(self,data,prev):
#         self.data=data
#         self.prev=data
#
# x = LinkedList(5)
# next(6,5)

# eg_dict = {key:value,key:value}
# eg_dict = {1:'Vedansh','class':5}
# print(eg_dict)
# print(eg_dict['class'])

# n = input('Name: ')
# a = int(input('Age: '))
#
# details_dict = {}
# details_dict['name']=n
# details_dict['age']=a
# print(details_dict)

# def func(arg):
#     if (123 % 2==0):
#         return True
#     else:
#         return False
#
# x = func(123)
# print(x)
#
# print(func(123))
#
# if (func(123)):
#     print()

# import qrcode

# def gen_qr(data):
#     qr = qrcode.QRCode()
#     qr.make(data)
#     img=qr.make_image(fill_color='black',back_color='white')
#     img.save('qr_img.png')
#     return 'Generated'
# text = input('Enter the content: ')
# print(gen_qr(text))

# List Tuple
# []     ()
(1,2,3,4,5)
(1,23.5,'vedansh')
my_tuple=('vedansh','Bansal')
print(my_tuple[0])
# Mutability
my_list = ['Vedansh','Bansal']
my_list[0]='Python'
print(my_list)

my_tuple = ('Vedansh','Bansal')
# my_tuple[0]='Python'
my_tuple = ('Python','Bansal')




