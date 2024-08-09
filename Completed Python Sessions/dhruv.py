# height = int(input('Enter your height'))
# if (height>100):
#     print('Enjoy the ride')
#
# p1 = input('Enter your option R(rock) or P(paper) or S(scissor)')
# p2 = input('Enter your option R(rock) or P(paper) or S(scissor)')
#
# if (p1=='R' and p2=='S'):
#     print('p1 wins')
# elif (p1=='S' and p2=='R'):
#     print('p2 wins')
# elif

# def Sanoj():
#     pass
#
# Sanoj()

# step 1 declare a variable and store a password as a string
# step 2 declare one more var and get user input asking for the password
# step 3 if condition is to check whether the saved password and the user password are same
# step 4a print success
# step 4b print fail or wrong password

# step 1 declare a variable and store a password as a string
# step 2 declare one more var and store and empty string
# step 3 while condition to make sure this runs until the right password is given
# step 4 declare one more var and get user input asking for the password
# step 5 if condition is to check whether the saved password and the user password are same
# step 5a print success
# step 5b print fail or wrong password

# def sanoj():
#     print('OK')
#     # return 'Something'
#
# print(sanoj())

# def dhruv():
#     if ():
#         return ('p1 win')
#     return 123

# a = dhruv()
# print(dhruv())

# dhruv(10,20) #pass by value
# a = 10
# b = 20
# dhruv(a,b) #pass by ref

# def addition():
#     a = 123
#     b = int(input('Enter a no'))

# dhruv1 = 'Sanoj' #gloabl variable

# def dhruv():
#     sanoj = 'dhruv' #local

# print(sanoj)

# 1x2=2
# 2x2=4
# 6

# name = input('Enter a name')
# place = input('enter a place')
# time = input('enter a time period')
# print(f"Hi my name is {name} I'm went to this {place} in {time}" )

# List= [1,2,3,4,5]
# Tuple = (1,2,3,4,5)
# print(List)
# List[2]='Three'
# Tuple[2]='Three'
# print(List)

# {key1:value1},{key2:value2},{key3:value3}
# {1:11},{'name':'dhruv'},{'marks':[1,2,3]}

# student_name = input('name: ')
# eng_mark = int(input('English marks: '))
# tam_mark = int(input('Tamil marks: '))
# math_mark = int(input('Maths marks: '))
# sci_mark = int(input('Science marks: '))
# soc_mark = int(input('Social marks: '))
#
# total_marks = eng_mark + tam_mark + math_mark + sci_mark + soc_mark
#
# print(f"""
# Hi, {student_name}
#
# Report card:
# English: {eng_mark}/100
# Tamil: {tam_mark}/100
# Maths: {math_mark}/100
# Science: {sci_mark}/100
# Social: {soc_mark}/100
# Total: {total_marks}/500
# """)

# Prime no or not
# def checkPrime(num):
#     for i in range(2,num):
#         if (num % i == 0):
#             return "not prime"
#     return "Prime"
#
# number = int(input('Enter a number'))
# print(checkPrime(number))

# even and odd from a list

# list_of_nos = input('enter few numbers').split()
# print(list_of_nos)
# even_list = []
# odd_list = []
# for each in list_of_nos:
#     if (int(each) % 2 == 0):
#         even_list.append(each)
#     else:
#         odd_list.append(each)
# print('Even List: ',even_list)
# print('Odd List: ',odd_list)

# to create a student mark details with dictionary
# {'dhruv':[100,100,100,100,100],'name2':[]}
# student_details = {} #part 1
# while(True):
#     user_choice = int(input('\n1.Add\n2.Exit\nyour option: ')) #part 2
#     if (user_choice == 1): #part 3a
#         name = input('Enter the name: ') #part 4
#         marks = input('Enter the marks: ').split() #part 5
#         student_details[name]=marks #part 6 packing the data inside dictionary
#     elif (user_choice == 2): #part 3b
#         print(student_details) #part 4 printing the dictionary
#         break #this is for exit

# f = open('dhruv.txt','w')
# f.write('Hi Im Dhruv Sanoj')
# f.close()
#
# f=open('dhruv.txt')
# print(f.read())
# f.close()

# print('*****\n****\n***\n**\n*')
# for i in range(5):
#     for j in range(5-i):
#         print('*',end='')
#     print()

# eg_dict = {'name':'dhruv'}
# # print(eg_dict['age']) #keyerror
#
# eg_list = [1,2,3,4,5]
# # eg_list.remove(10) #value error
#
# # eg_list.removes(2) #attribute error
#
# # print(dhruv) #name error
#
# # print('5' + 10) #type error
year = 2024
year -= 11
print(year)