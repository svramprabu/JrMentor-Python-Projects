# for iterating_var in sequence:
#     Statement


# paragraph = input('Enter / Paste the para here: ')
# words = paragraph.split()
# n = 0
# for each_word in words:
#     n += 1 #n+1
# print(f"Number of words present in the paragraph is {n}")

# Acronym Generator using for loop
# United Nations UN
# United States US
# Indian Space Research Organization ISRO

# user_input = input('Enter here: ')
# words = user_input.split()
# ans = ''
# for each_word in words:
#     ans += each_word[0].upper() #I S R O
# print(f"Acronym for {user_input} is {ans}")

# nums = [12,23,3456,34,67]
#
# for each_num in nums:
#     if (each_num % 2 == 0):
#         print(f"{each_num} is an even number")
#     else:
#         print(f"{each_num} is an odd number")

# s = "Python Programming"
# for ch in s:
#     print(ch)

# s = input("enter string: ")
# ltr = input('enter letter: ')
# answer = 0
# for ch in s:
#     if (ch == ltr):
#         answer += 1
# print(f"Number of times {ltr} occured in {s} is {answer}")

# s = input('enter string: ') #environment -> enviromt
# answer = ''
# for ch in s:
#     if (ch.lower() not in answer):
#         answer += ch.lower()
# print(f"Before: {s}")
# print(f"After: {answer}")

# s = input('Enter string: ')
# vowels = "aeiou"
# ans = 0
# for ch in s:
#     if (ch.lower() in vowels):
#         ans += 1
# print(f"Number of vowels in {s} is {ans}")

# for i in range(10):
#     print(i)
#
# for i in range(1,20):
#     print(i)
#
# a = 10
# b = 50
# for i in range(a,b):
#     print(i)

# 1 x 2 = 2
# 2 x 2 = 4
# 3 x 2 = 6

n = int(input('Enter table_no: '))
for i in range(1,11):
    print(f"{i} X {n} = {i*n}")