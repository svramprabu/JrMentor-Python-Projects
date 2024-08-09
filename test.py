# board = [' ' for _ in range(9)]
#
# for i in range(3):
#     # [' ',' ',........]
#     # 0 1 2-> i*3 -> 0 3 6 : (i+1)*3-> 3 6 9
#     print('|'+'|'.join(board[i * 3:(i + 1) * 3])+'|')
#
#
# # print(''.join(['H','e','l','l','o']))
# #  |0|1|2|
# #  |3|4|5|
# #  | | | |

# for i in range(3):
#     nums = []
#     for j in range(i * 3, (i + 1) * 3):
#         nums.append(str(j))
#     print('|'+'|'.join(nums)+'|')

# cycle 1
# i = 0                       1               2
# nums = []                   []              []
# range(0,3)                  (3:6)           (6:9)
# nums = ['0']                ['3']
# nums = ['0','1']
# nums = ['0','1','2']
# print(nums)


import numpy
# import numpy as np
# arr = np.array([1,2,3],ndmin=2)
# res = arr*2
# print(res)



n = input('What is your name: ')
print('My name is',n)






























