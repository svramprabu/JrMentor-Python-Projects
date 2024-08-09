# saved_password = 'tanish123'
# print('Hi, Tanish')
# user_input = input('Please enter your password: ')
# if (user_input == saved_password):
#     print('Welcome')
# else:
#     print('Sorry, wrong password')

# declare two variables and get user input to store
# current year and year of birth
# calculate and print the age
# if age is more than 10 print Big boy
# else print small boy

# current_year = int(input('Enter the current year')) # declared a variable to store current year
# year_of_birth = int(input('Enter the year of birth')) # declare a variable to store year of birth
# age = current_year - year_of_birth # calculated the age
# print(age) # printed the calculated age
#
# if (age>10): # if age is more than 10
#     print('Big boy')
# elif (age==10):
#     print('Tanish age')
# else:
#     print('small boy')

# list_of_toys = ['cycle','bike','cars','train']
# print(list_of_toys)
# for x in list_of_toys:
#     print(x)

# i+=1 #i=i+1
# i+=2 #i=i+2
# i+=3 #i=i+3

# i = 0
# while (i<10):
#     i += 1
#     if i==4:
#         pass
#     print(i)

# def tanish():
#     print('Tanish is a good boy')
#
# tanish()

# user_name = input('Enter your name')
# fav_animal = input('enter your favourite animal')
# fav_spot = input('Enter your fav spot')
# print(f'My name is {user_name}. My favourite animal is {fav_animal} and I wish to visit {fav_spot}')


# print(f'Once upon a time, in a peaceful {place}, there lived a {animal} who loved to show off his {talent} and a slow, patient {friend}. Once the {friend} decided to challenge the hare to a {competition}, The {name} agreed to race, thinking it would be an easy victory.')

# Multiplication table
# table_no = int(input('Enter the table no'))
# for i in range(1,13):
#     print(f'{i} x {table_no} = {i * table_no}')

# a = 10 #global variable

# def exam():
#     global b
#     b = 15
#
# def test():
#     c = 100 #local variable
#
# def fn1():
#     d = 20 #local variable
#     def fn2():
#         e = 30 #non local variable

# Words counter
# user_data = input('enter your data: ').split()
# number_of_words = len(user_data)
# print(f"You have {number_of_words} words in user data")

#student report
# student_name = input('enter the name')
#
# marks = []
# for i in range(5):
#     subject_mark = int(input('enter the marks'))
#     marks.append(subject_mark)
#
# total_marks = marks[0] + marks[1] + marks[2] + marks[3] + marks[4]
#
# print(f"Hi {student_name}, you have scored a total of {total_marks} in the exam.")

# def checkPrime (number):
#     for i in range(2,number):
#         if (number % i == 0): #x == y
#             return f'{number} is not a prime number'
#     return f"{number} is a prime number"
#
# n = int(input('Enter a number: '))
# print(checkPrime(n))

# # Todo list project
# list_of_tasks = []
# print('Welcome to my Todo list project')
# while (True):
#     option = int(input('\n1.Add a task\n2.Remove a task\n3.search a task\noption: '))
#
#     if (option == 1):
#         task = input('Name of the task: ')
#         if (task not in list_of_tasks):
#             list_of_tasks.append(task)
#             print('task added successfully')
#         else:
#             print('task is a duplicate')
#
#     elif (option == 2):
#         task = input('Name of the task to remove: ')
#         if (task in list_of_tasks):
#             list_of_tasks.remove(task)
#             print('task removed successfully')
#         else:
#             print('task not found')
#
#     elif (option == 3):
#         task = input('Name of the task to search: ')
#         if (task in list_of_tasks):
#             print('task found')
#         else:
#             print('task not found')

# Program to check whether a string is a palindrome
# n = input('Enter the string: ')
# ans = ''
# for i in n:
#     ans = i+ans
# print(n,ans)
# if n == ans:
#     print('Palindrome')
# else:
#     print('not a palindrome')

# Slicing
# Dictionary

# s = input('Enter: ')
# letter = input('Letter: ')
# ans=0
# for each_letter in s:
#     print(each_letter)
#     if (each_letter == letter):
#         ans+=1
# print(f"We have {ans} {letter} in {s}")


# # To count the number of vowels in the given string
# s = input('Enter: ')
# vowels = 'aeiou'
# ans=0
# for each_letter in s:
#     print(each_letter)
#     if (each_letter.lower() in vowels):
#         ans+=1
# print(f"We have {ans} vowels in {s}")
#
# s = input('Enter: ')  # Tanish Velavan
# ans = []
# for curr_index in range(len(s)):
#     print('Current letter:', s[curr_index], 'Remaining string:', s[curr_index + 1:])
#     if (s[curr_index] in s[curr_index + 1:]):
#         if (s[curr_index] not in ans):
#             ans.append(s[curr_index])
# print(f'Duplicate characters in {s} are {ans}')

f = open('tanish.txt','w')
f.write("I am a good student")
f.close()

f = open("tanish.txt")
print(f.read())

